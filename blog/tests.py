#  -*- coding:utf-8 -*-
"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from models import Column,Tag,Article,Comment
from user.models import User
import hashlib
from datetime import datetime


class SimpleTest(TestCase):
    def testModels(self):
        """


        """
        user = User()
        user.username='admin'
        user.nickname='管理员'
        m = hashlib.md5()
        m.update('890106')
        user.password=m.hexdigest()
        user.lastLoginTime=datetime.today()
        user.registerTime=datetime.today()
        user.save()

        user2 = User()
        user2.username='roy'
        user2.nickname='飞越海面'
        m = hashlib.md5()
        m.update('890106')
        user2.password=m.hexdigest()
        user2.lastLoginTime=datetime.today()
        user2.registerTime=datetime.today()
        user2.save()

        user3 = User()
        user3.username='wanghan'
        user3.nickname='汪晗'
        m = hashlib.md5()
        m.update('890106')
        user3.password=m.hexdigest()
        user3.lastLoginTime=datetime.today()
        user3.registerTime=datetime.today()
        user3.save()

        print User.objects.all()
        print User.objects.get(id='1').lastLoginTime
        print User.objects.filter(username='admin',nickname='管理员')
        print User.objects.filter(username__startswith='a').exclude(blognum__gt=0)

        #user.focusUsers.add(user2)
        user.focusUsers.add(user3)
        user2.focusUsers.add(user3)
        #user3.focusUsers.add(user2)

        user.save()
        user2.save()
        user3.save()

        print user.focusUsers.all()

        print "%s's funs number %d" % (user.username,user.focusUsers.count())
        print "%s's funs number %d" % (user2.username,user2.focusUsers.count())
        print "%s's funs number %d" % (user3.username,user3.focusUsers.count())

        col=Column()
        col.name='Java技术'
        col.owner=user2
        col.save()

        tag=Tag()
        tag.name='Java'
        tag.save()

        tag2=Tag()
        tag2.name='Hibernate'
        tag2.save()

        article=Article()
        article.title='Hibernate怎么样啊'
        article.content='大家说说，Hibernate怎么样啊'
        article.owner=user2
        article.column=col
        article.publishTime=datetime.today()
        article.save()

        article.tags.add(tag)
        article.tags.add(tag2)
        article.save()

        comm=Comment()
        comm.content="我觉得很好用啊"
        comm.article=article
        comm.publishTime=datetime.today()
        comm.publisher=user3
        comm.save()

        comm1=Comment()
        comm1.content="是吗？仔细说说"
        comm1.article=article
        comm1.publishTime=datetime.today()
        comm1.publisher=user2
        comm1.refcomment=comm
        comm1.save()

        print Comment.objects.filter(article=article)
        print Comment.objects.filter(publisher=user3)[0].content



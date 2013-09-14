#  -*- coding:utf-8 -*-
from django.db import models
from user.models import User

class Column(models.Model):
    class Meta:
         db_table = 'blog_column'
    name=models.CharField(max_length=100)
    owner=models.ForeignKey(User)
    articlenum=models.IntegerField(default=0)

class Tag(models.Model):
    class Meta:
         db_table = 'blog_tag'
    name=models.CharField(max_length=100)
    active=models.IntegerField(default=0)
    def __unicode__(self):
        return self.name

class Article(models.Model):
    class Meta:
         db_table = 'blog_article'
    title=models.CharField(max_length=100)
    content=models.TextField()
    publishTime=models.DateTimeField()
    owner=models.ForeignKey(User)
    column=models.ForeignKey(Column)
    tags=models.ManyToManyField(Tag)
    goodnum=models.IntegerField(default=0)
    badnum=models.IntegerField(default=0)
    visitnum=models.IntegerField(default=0)
    commentnum=models.IntegerField(default=0)

class Comment(models.Model):
    class Meta:
         db_table = 'blog_comment'
    content=models.TextField()
    publishTime=models.DateTimeField()
    publisher=models.ForeignKey(User)
    article=models.ForeignKey(Article)
    refcomment=models.ForeignKey('self',null=True)


from django.db import models

class User(models.Model):
    class Meta:
         db_table = 'user'
    username=models.CharField(max_length=100)
    nickname=models.CharField(max_length=100)
    password=models.CharField(max_length=100)
    registerTime=models.DateTimeField()
    lastLoginTime=models.DateTimeField()
    fansnum=models.IntegerField(default=0)
    blognum=models.IntegerField(default=0)
    commentnum=models.IntegerField(default=0)
    desc=models.CharField(max_length=1000)
    favorite=models.CharField(max_length=200)
    logo=models.CharField(max_length=1000)
    focusUsers=models.ManyToManyField('self',symmetrical=False,db_table='user_focus_users')
    def __unicode__(self):
        return self.username

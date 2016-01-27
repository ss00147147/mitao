# -*- coding:utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from DjangoUeditor.models import UEditorField

# Create your models here.
class MyPerson(models.Model):
    name = models.CharField('姓名',max_length=30)
    password = models.CharField('外号',max_length=30)
    
    def __unicode__(self):
        return self.name

class news(models.Model):
    content = UEditorField('内容',height=300,width=1000,default=u'',blank=True)
    
    def __unicode__(self):
        return self.content

class TourGroup(models.Model):    
    Title = models.CharField('标题',max_length=30)
    # User_id = models.ForeignKey(User,related_name='UserId_TourGroup')
    Cover = models.FileField(default="",upload_to='cover/%Y/%m/%d/')
    Exclusive = models.FileField(default="",upload_to='exclusive/%Y/%m/%d/')
    Abstract = models.CharField('摘要',default="",max_length=100)
    Description = models.CharField('描述',default="",max_length=1000)   
    TripMode = models.CharField('行程安排',default="",max_length=1000)
    Notice = models.CharField('注意事项',default="",max_length=1000)
    def __unicode__(self):  
        return self.Title

    

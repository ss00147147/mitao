#coding:utf-8
from django import forms

class AddForm(forms.Form):
    name = forms.CharField(max_length=30)
    password = forms.CharField(max_length=30)

class travelenter(forms.Form):
    Title = forms.CharField(initial = '请输入标题',max_length=30)
    Abstract = forms.CharField(initial = '请输入摘要',max_length=100)
    Cover = forms.FileField()
    Exclusive = forms.FileField()
    Description = forms.CharField(initial = '请输入描述',widget=forms.Textarea,max_length=1000)
    # ImgAddress1 = forms.FileField(upload_to='mitaoapp/templates/upload/')
    # ImgAddress2 = forms.FileField(upload_to='mitaoapp/templates/upload/')
    # ImgAddress3 = forms.FileField(upload_to='mitaoapp/tem    # LookPoints = forms.CharField(widget=forms.Textarea,max_length=1000)
    TripMode = forms.CharField(initial = '请输入行程',widget=forms.Textarea,max_length=1000)
    Notice = forms.CharField(initial = '请输入须知',widget=forms.Textarea,max_length=1000)

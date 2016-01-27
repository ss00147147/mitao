
from django.http import HttpResponse
from django.shortcuts import render
from django import forms
from .forms import AddForm
from .forms import travelenter
from .models import *
import Image


# -*- coding: utf-8 -*-
# Create your views here.

def register(request):
    if request.method == 'POST':
        form = AddForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            password = form.cleaned_data['password']
            if request.POST.has_key('register'):
                twy = MyPerson.objects.filter(name=name)
                if twy:
                    return render(request, 'register_login.html', {'result': ''})
                else:
                    twz = MyPerson(name=name,password=password)   #age=str(int(a) + int(b))
                    twz.save()
                    return render(request, 'register_login.html', {'result': ''})
            elif request.POST.has_key('login'):
                twq = MyPerson.objects.filter(name=name).filter(password=password)
                if twq:
                    #return HttpResponse(str(int(a) + int(b)))
                    return render(request, 'register_login.html', {'result': ''})
                else:
                    return render(request, 'register_login.html', {'result': ''})
    else:
        form = AddForm
    return render(request, 'register_login.html', {'form':form})

def login(request):
    return render(request, 'register_login.html')




def traveledit(request):
    if request.method == 'POST':
        tf = travelenter(request.POST, request.FILES)
        if tf.is_valid():
            Title = tf.cleaned_data['Title']
            Cover = tf.cleaned_data['Cover']
            Abstract = tf.cleaned_data['Abstract']
            Description = tf.cleaned_data['Description']
            TripMode = tf.cleaned_data['TripMode']
            Notice = tf.cleaned_data['Notice']
            Exclusive = tf.cleaned_data['Exclusive']    
            
            if request.POST.has_key('ok'):
                te = TourGroup.objects.filter(Title=Title)
                if te:
                    return render(request, 'buy_detail_edit.html', {'result': ''})
                else:
                    tff=TourGroup()
                    tff.Title=Title
                    tff.Cover=Cover
                    tff.Abstract=Abstract
                    tff.Description=Description
                    tff.TripMode=TripMode
                    tff.Notice=Notice
                    tff.Exclusive=Exclusive
                    tff.save()
                    return render(request, 'buy_detail_edit.html', {'result':''})
          
    else:
        tf = travelenter()

    return render(request, 'buy_detail_edit.html', {'tf':tf})


def travellist(request):
    travelviewlists=TourGroup.objects.all()
    return render(request, 'list.html', {'travelviewlists': travelviewlists})

def traveldetail(request,detail_id):
    travelviewdetails = TourGroup.objects.get(id=detail_id)
    # tee = TourGroup.objects.filter(id=detailid)
    # travelviewdetails=TourGroup(Title=Title,Abstract=Abstract,Description=Description,TripMode=TripMode,Notice=Notice)
    # travelviewdetails = TourGroup.objects.all()
    return render(request, 'buy_detail.html', {'travelviewdetails': travelviewdetails})





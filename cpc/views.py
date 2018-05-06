# -*- coding: utf-8 -*-
from __future__ import unicode_literals

# from django.shortcuts import render
from django.core.mail import BadHeaderError, EmailMessage
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import ContactForm
from cpc.models import Events
# Create your views here.

def index(request):
    return render(request,'cpc/home.html')

# def contact(request):
#     return render(request,'cpc/contact.html')

def contact(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            contact_name = form.cleaned_data['contact_name']
            contact_email = form.cleaned_data['contact_email']
            content = form.cleaned_data['content']
            try:
                email = EmailMessage(contact_name,
                                    content,
                                    contact_email,
                                    ['geetgonnarock@gmail.com'], #change to your email
                                     reply_to=[contact_email],
                                   )
                email.send()
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('/thanks')
    return render(request, 'cpc/contact.html', {'form': form})


def thanks(request):
    thanksVar = "Thank you so much!! We have sent an email to the admin for you. :D"
    return render(request, 'cpc/thanks.html', {"thanksVar" : thanksVar})

def events(request):
    eData = Events.objects.all()
    return render(request, 'cpc/events.html', {"eventsData" : eData})

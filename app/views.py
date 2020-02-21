from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic import CreateView
from app.models import *


class Landing(TemplateView):
    template_name = 'index.html'


class Contact(TemplateView):
    template_name = 'contact.html'


class Form(CreateView):
    model = Skillset
    template_name = 'form.html'
    fields = ['company_name', 'company_size', 'location',
              'remote_work', 'language_requirement']

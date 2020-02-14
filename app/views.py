from django.shortcuts import render
from django.views.generic.base import TemplateView

class Hello(TemplateView):
    template_name = 'index.html'


class Contact(TemplateView):
    template_name = 'contact.html'
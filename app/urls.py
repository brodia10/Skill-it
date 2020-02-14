from django.urls import path, include
from . import views
from .views import *

app = 'app'

urlpatterns = [
    path('', Hello.as_view(), name='Hello'),
	path('contact', Contact.as_view(), name='Contact'),
]
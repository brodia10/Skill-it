from django.urls import path, include
from . import views
from .views import *

app = 'app'


urlpatterns = [
    path('', Landing.as_view(), name='Landing'),
    path('form', Form.as_view(), name='Form')
]

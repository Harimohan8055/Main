from django.urls import path
from . import views

urlpatterns =[
    path('', views.home, name='TechE&I-Home'),
]

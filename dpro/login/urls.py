from django.urls import path
from . import views

urlpatterns = [
    path('', views.login, name='TechE&I-Login'),
    path('register', views.register,name='TechE&I-Register'),
]

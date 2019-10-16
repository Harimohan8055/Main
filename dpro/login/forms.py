from django import forms
from .models import *

TYPE=[
    ('','------Select-----'),
    ('individual','Individual'),
    ('institutions','institutions'),
    ('companies','companies')
]
class register_form(forms.Form):
    user_type=forms.CharField(label='User Type', widget=forms.Select(choices=TYPE))
    fullname=forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Enter Your Name'}), max_length=50)
    email = forms.CharField(widget=forms.EmailInput(attrs={'placeholder':'Enter Email Id'}), max_length=50)
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'**********'}), max_length=50)
    repeat_password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'**********'}), max_length=50)

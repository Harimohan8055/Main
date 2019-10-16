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
    mobno = forms.CharField(widget=forms.NumberInput(attrs={'placeholder':'Enter Mobile Number'}), max_length=50)
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'********** Minimum Size 8'}), max_length=50)
    repeat_password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'********** Minimum Size 8'}), max_length=50)


    def clean(self):
        cleaned_data = super(register_form, self).clean()
        password = cleaned_data.get('password')
        repeat_password = cleaned_data.get('repeat_password')
        if password != repeat_password:
            raise forms.ValidationError("Password Doesnot Match")
        else:
            if len(password)<8:
                raise forms.ValidationError("Password Too short")

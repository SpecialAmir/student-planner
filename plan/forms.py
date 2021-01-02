from django import forms
from .models import Plan
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
class PlanForm(forms.ModelForm):

    class Meta:
        model = Plan
        exclude = ['user']

class RegisterForm(UserCreationForm):
    username = forms.CharField(widget = forms.TextInput(attrs = {'class':'form-control',
        'placeholder':'نام کاربری'

        }))
    password1 = forms.CharField(widget = forms.PasswordInput(attrs = {
        'class':'form-control',
        'placeholder':'رمز عبور'
        }))
    password2 = forms.CharField(widget = forms.PasswordInput(attrs = {
        'class':'form-control',
        'placeholder':'تکرار رمز عبور'
        }))


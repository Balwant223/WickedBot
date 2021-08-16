from django import forms
from django.db import models
from django.forms import fields
from .models import User

class UserDetailsForm(forms.ModelForm):
    class Meta:
        model=User
        fields='__all__'
from django import forms
from django.contrib.auth.models import User

from django.contrib.auth.forms import UserCreationForm
from .models import UserProfile

class RegistrationForm(UserCreationForm):
    role = forms.ChoiceField(choices=[('student', 'Student'), ('staff', 'Staff'), ('admin', 'Admin'), ('editor', 'Editor')])
    country = forms.CharField(max_length=255)
    nationality = forms.CharField(max_length=255)
    mobile = forms.CharField(max_length=15)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'role', 'country', 'nationality', 'mobile']

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['role', 'country', 'nationality', 'mobile']

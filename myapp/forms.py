# from django import forms
# from django.contrib.auth.forms import AuthenticationForm

# class CustomLoginForm(AuthenticationForm):
#     username = forms.CharField(widget=forms.TextInput(attrs={
#         'class': 'form-control',
#         'placeholder': 'Username'
#     }))
#     password = forms.CharField(widget=forms.PasswordInput(attrs={
#         'class': 'form-control',
#         'placeholder': 'Password'
#     }))

from django import forms
from django.contrib.auth.models import User
from .models import Profile

class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email']

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['bio', 'location', 'birth_date', 'profile_picture']

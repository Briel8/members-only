from django import forms
from django.contrib.auth.models import User
from .models import Post

class SignUpForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'username', 'password']
        widgets = {
            'password': forms.PasswordInput()   
        }

class LogInForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']
        widgets = {
            'password': forms.PasswordInput()   
        }

class AddPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']
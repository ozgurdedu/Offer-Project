from django import forms
from django.contrib.auth.models import User


class RegisterForm(forms.ModelForm):
    email = forms.CharField(
        max_length=255,
        required=True,
        widget=forms.EmailInput(
            attrs={'class': 'form-control', 'placeholder': 'Email'}),
        )
    username = forms.CharField(
        max_length=25,
        required=True,
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': 'Username'}),
        )
    password1 = forms.CharField(
        max_length=25,
        required=True,
        widget=forms.PasswordInput(
            attrs={'class': 'form-control', 'placeholder': 'Password'}),
        )
    password2 = forms.CharField(
        max_length=25,
        required=True,
        widget=forms.PasswordInput(
            attrs={'class': 'form-control', 'placeholder': 'Password Again'}),
        )
    first_name = forms.CharField(
        max_length=25,
        required=True,
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': 'First Name'}),
        )
    last_name = forms.CharField(
        max_length=25,
        required=True,
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': 'Last Name'}),
        )
    
    class Meta:
        model = User
        fields = ['email', 'username', 'password1', 'password2', 'first_name', 'last_name']    



class LoginForm(forms.Form):
    username = forms.CharField(
        max_length=150, 
        label='Kullanıcı Adı',  
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': 'Password'}
        ))
    
    password = forms.CharField(label='Şifre', widget=forms.PasswordInput(
            attrs={'class': 'form-control', 'placeholder': 'Password'}))
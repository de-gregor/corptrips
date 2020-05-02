from django import forms
from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import (
    authenticate, 
    get_user_model,
     
)

User = get_user_model()

class UserLoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self, *args, **kwargs):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        if username and password:
            user = authenticate(username=username,password=password)
            if not user:
                raise forms.ValidationError('This user doesnot exist')
            if not user.check_password(password):
                raise forms.ValidationError('Incorrect password')
            if not user.is_active:
                raise forms.ValidationError('This user is not active')
        return super(UserLoginForm,self).clean(*args,**kwargs)

class UserRegistrationForm(forms.ModelForm):
    email = forms.EmailField(label='Email Adress',widget=forms.EmailInput)
    password = forms.CharField(widget=forms.PasswordInput)
    password_confirm = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = [
            'username', 
            'email', 
            'password',
            'password_confirm'
            ]
    
    def clean(self):
        password = self.cleaned_data('password')
        password_confirm = self.cleaned_data('password_confirm')
        username = self.cleaned_data('username')
        
        if password != password_confirm:
            raise forms.ValidationError('passwords must match!')
        username_eq = User.objects.filter(username=username)
        if username_eq.exist():
            raise forms.ValidationError('username already exists!')
        return username


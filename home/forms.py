from django import forms

from .models import Student
from django.contrib.auth.models import User

class StudentEditModelForm(forms.ModelForm):
    class Meta:
        model=Student
        fields="__all__" #student_name.department
        widgets={
            'student_name': forms.TextInput(attrs={'class':'form-control','placeholder':'Student Name'}),
            'department':forms.Select(attrs={'class':'custom-select'})
        }

class StudentCreateForm(forms.Form):
    student_name=forms.CharField(label='', 
            widget=forms.TextInput(
                attrs={'class':'form-control','maxlength':'50','placeholder':'Student Name'}))
    dept=(('CSE','COMPUTER SCIENCE'),('MH','MECHANICAL'),('CV','CIVIL')) 
    department=forms.CharField(label='', widget=forms.Select(attrs={'class':'form-control'},choices=dept))       


class StudentSearchForm(forms.Form):
    q=forms.CharField(label='',widget=forms.TextInput(attrs={'class':'form-control','maxlength':'30','placeholder':'Search'}))

class LoginForm(forms.Form):
    r=forms.CharField(label='login',widget=forms.TextInput(attrs={'class':'form-control','maxlength':'30','placeholder':'login'}))

class UserRegistrationForm(forms.ModelForm):
    password=forms.CharField(label='Password',widget=forms.PasswordInput(attrs={'class':'form-control'}))
    class Meta:
        model=User
        fields=('username','first_name','last_name','email','password')
        widgets={
            'username':forms.TextInput(attrs={'class':'form-control','autofocus':'true'}),
            'first_name':forms.TextInput(attrs={'class':'form-control'}),
            'last_name':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.EmailInput(attrs={'class':'form-control'})
        }
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *
from django import forms
from django.forms.widgets import TextInput  , EmailInput , PasswordInput , NumberInput
from django.forms import inlineformset_factory


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2']
        widgets = {
            'username': TextInput(attrs={'class': 'input100','placeholder':'User name'}),
            'email': EmailInput(attrs={'class': 'input100','placeholder':'User name'}),
            'first_name': TextInput(attrs={'class': 'input100','placeholder':'User name'}),
            'last_name': TextInput(attrs={'class': 'input100','placeholder':'User name'}),
            'password1': PasswordInput(attrs={'class': 'input100','placeholder':'User name'}),
            'password2': PasswordInput(attrs={'class': 'input100','placeholder':'User name'}),
            }

class StudentObj(forms.ModelForm):
    class Meta:
        model = Student
        fields = "__all__"
        exclude = ['user',"Department_DS","Department_SVM","Department_KNN" ,"DS_acc",
                   "SVM_acc" , "KNN_acc"]

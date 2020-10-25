from django.forms import ModelForm, Textarea
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from .models import Order
from .models import ContactMail




class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = [
                'username',
                'email',
                'password1',
                'password2'
        ]

class CreateOrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = [
            'name',
            'email',
            'phone',
            'location',
            'datetime',
        ]
        widgets = {
            'datetime': 
                        forms.DateTimeInput(attrs={
                            'input_formats' : ['%d/%m/%Y %H:%M'],
                            'class': 'form-control datetimepicker-input',
                            'data-target': '#datetimepicker1'
                            }),
           
        }

class CreateContactForm(forms.ModelForm):
    class Meta:
        model = ContactMail
        fields = [
            'User_name',
            'User_email',
            'User_msg',

        ]


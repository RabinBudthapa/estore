from django import forms
from .models import OrderDetail
from django.contrib.auth.models import User


class CheckoutForm(forms.ModelForm):
    class Meta:
        model = OrderDetail
        fields = ['firstname', 'lastname', 'email', 'phone_number', 'address', 'payment_method']

        labels = {
            'firstname': 'First Name',
            'lastname': 'Last Name',
            'email': 'Email Address',
            'phone_number': 'Phone Number',
            'address': 'Address',
            'payment_method': 'Payment Method',
        }

        widgets = {
            'firstname': forms.TextInput(attrs={'placeholder': 'First Name', 'class': 'form-control'}),
            'lastname': forms.TextInput(attrs={'placeholder': 'Last Name', 'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Email', 'class': 'form-control'}),
            'phone_number': forms.TextInput(attrs={'placeholder': 'Phone Number', 'class': 'form-control'}),
            'address': forms.TextInput(attrs={'placeholder': 'Address', 'class': 'form-control'}),
            'payment_method' : forms.RadioSelect(choices=OrderDetail.PAYMENT_CHOICES,attrs={'class': 'payment-methods'})

        }
    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super(CheckoutForm, self).__init__(*args, **kwargs)
        if user:
            self.fields['firstname'].initial = user.first_name
            self.fields['lastname'].initial = user.last_name
            self.fields['email'].initial = user.email


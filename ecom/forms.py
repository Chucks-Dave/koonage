from pyclbr import Class
from django import forms
from django.contrib.auth.models import User
from .models import *


class CustomerUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'password']
        widgets = {
            'password': forms.PasswordInput()
        }


class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['address', 'mobile', 'profile_pic']


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'price', 'description', 'product_image']

# address of shipment


class AddressForm(forms.Form):
    Email = forms.EmailField()
    Mobile = forms.IntegerField()
    Address = forms.CharField(max_length=500)


class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['name', 'feedback']

# for updating status of order


class OrderForm(forms.ModelForm):
    class Meta:
        model = Orders
        fields = ['status']

# for contact us page


class ContactusForm(forms.Form):
    Name = forms.CharField(max_length=30)
    Email = forms.EmailField()
    Message = forms.CharField(
        max_length=500, widget=forms.Textarea(attrs={'rows': 3, 'cols': 30}))


class AppointmentForm(forms.ModelForm):

    class Meta:
        model = Appointment

        fields = ['date', 'time', 'staff_member',
                  'customer', 'email', 'message']


class CouponForm(forms.Form):
    code = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control'}))

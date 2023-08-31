from django import forms
from .models import ShippingDetails


class ShippingForm(forms.ModelForm):
    name = forms.CharField(max_length=150, required=True)
    city = forms.CharField(max_length=70,  required=True)
    address = forms.CharField(max_length=200,  required=True)
    email = forms.EmailField()

    class Meta:
        model = ShippingDetails
        fields = ['name', 'city', 'address', 'email']

from django import forms

from .models import Address, Order

class AddrForm(forms.ModelForm):
    
    class Meta:
        model = Address
        fields = ['addr',]
    
class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['quantity', ]
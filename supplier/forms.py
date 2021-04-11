from django import forms

from store.models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'unitprice', 'rem_quant']
        labels = {'name': 'Procut Name',}
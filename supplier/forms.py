from django import forms

from store.models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
            'name', 
            'category', 
            'unitprice', 
            'rem_quant', 
            'description',
            'image',
        ]
        labels = {
            'name': 'Product Name',
        }
from django.contrib import admin

# Register your models here.
from .models import Product
from .models import Supplier

admin.site.register(Product)
admin.site.register(Supplier)
from django.contrib import admin

# Register your models here.
from .models import Product, Order, Category
from .models import Supplier

admin.site.register(Product)
admin.site.register(Supplier)
admin.site.register(Order)
admin.site.register(Category)
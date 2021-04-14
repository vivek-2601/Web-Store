from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Address(models.Model):
    """Address of a user"""
    # This can be changed from OnttoOne to ForignKey if we 
    # want our users to have multiple addresses.
    
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    addr = models.CharField(verbose_name="address", max_length=150)

class Product(models.Model):
    """A product is something user can buy."""
    # set id later on, as of now it added automatically

    name = models.CharField(max_length= 100)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    unitprice = models.PositiveIntegerField('Price')
    rem_quant = models.PositiveIntegerField(verbose_name = "quantity remaining")
    image = models.ImageField(upload_to='images', null= True)
    
    def __str__(self):
        """Return a string representtion of the model."""
        return self.name


class Order(models.Model):
    """Stores information about the placed order."""
    user       = models.ForeignKey(User, on_delete=models.CASCADE)
    quantity   = models.IntegerField()
    product    = models.ForeignKey(Product, on_delete=models.CASCADE)
    date       = models.DateTimeField(auto_now_add= True)

    def __str__(self):
        return self.product.name + '_' + str(self.quantity)
class Supplier(models.Model):
    """Suplier supplies product."""
    # set id later on

    name = models.CharField(max_length= 30)

    def __str__(self):
        return self.name


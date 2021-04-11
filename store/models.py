from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Product(models.Model):
    """A product is something user can buy."""
    # set id later on, as of now it added automatically

    name = models.CharField(max_length= 100)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    unitprice = models.PositiveIntegerField('Price')
    rem_quant = models.PositiveIntegerField(verbose_name = "quantity remaining")
    def __str__(self):
        """Return a string representtion of the model."""
        return self.name


class Supplier(models.Model):
    """Suplier supplies product."""
    # set id later on

    name = models.CharField(max_length= 30)

    def __str__(self):
        return self.name


from django.db import models

# Create your models here.
class Product(models.Model):
    """A product is something user can buy."""
    # set id later on

    name = models.CharField(max_length= 100)

    def __str__(self):
        """Return a string representtion of the model."""
        return self.name


class Supplier(models.Model):
    """Suplier supplies product."""
    # set id later on

    name = models.CharField(max_length= 30)

    def __str__(self):
        return self.name


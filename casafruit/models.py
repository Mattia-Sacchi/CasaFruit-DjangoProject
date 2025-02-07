from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100)  # Product name
    price = models.DecimalField(max_digits=6, decimal_places=2)  # Price with 2 decimal places
    description = models.TextField(blank=True, null=True)  # Optional description
    image = models.ImageField(upload_to='products/')  # Upload images to 'media/products/'

    def __str__(self):
        return self.name  # Show product name in Django Admin
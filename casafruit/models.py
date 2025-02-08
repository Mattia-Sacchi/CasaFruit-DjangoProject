from django.db import models
from django.contrib.auth.models import User
from django.db.models import UniqueConstraint

class Product(models.Model):
    name = models.CharField(max_length=100, primary_key=True)  # Product name
    price = models.DecimalField(max_digits=6, decimal_places=2)  # Price with 2 decimal places
    description = models.TextField(blank=True, null=True)  # Optional description
    image = models.ImageField(upload_to='products/')  # Upload images to 'media/products/'

    def __str__(self):
        return self.name  # Show product name in Django Admin
    def to_dict(self):
        return {
            'name': self.name,
            'price': self.price,
            'description': self.description,
            'image': self.image,

        }

class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=False)
    like = models.BooleanField(default=False)
    class Meta:
        constraints = [
            UniqueConstraint(fields=['user', 'product'], name='unique_review'),
        ]
    def __str__(self):
        temp = ""
        if self.like == True: 
            temp =  "positive"  
        else: 
            temp= "negative" 
        return f"Review by {self.user.username} of {self.product.name}, Rating " +temp
    def to_dict(self):
        return {
            'user' : self.user.username,
            'product' : self.product.name,
            'like' : self.like
        }
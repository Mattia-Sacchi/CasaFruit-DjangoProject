from django.contrib import admin

# Register your models here.
from .models import Product
from .models import Like

admin.site.register(Like)
admin.site.register(Product)
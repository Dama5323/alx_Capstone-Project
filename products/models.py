from django.db import models
from django.conf import settings  # To reference the custom user model

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    
    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    description = models.TextField(blank=True)
    stock = models.PositiveIntegerField(default=0)
    image = models.ImageField(upload_to='product_images/', blank=True, null=True)
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,  # Links to your CustomUser
        on_delete=models.SET_NULL,
        null=True,
        related_name='products'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
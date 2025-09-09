import uuid
from django.db import models

# Create your models here.
class Product(models.Model):
    CATEGORY_CHOICES = [
        ('clothing', 'Clothing'),
        ('accessories', 'Accessories'),
        ('shoes', 'Shoes'),
        ('skills', 'Skills'),
        ('superDuperUltraRareUnique Item', 'SuperDuperUltraRareUnique Item'),
    ]
    
    name = models.CharField(max_length=100, unique=True)
    price = models.IntegerField()
    description = models.TextField()
    thumbnail = models.URLField(blank=True, null=True)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    is_featured = models.BooleanField(default=False)
import uuid
from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

# Create your models here.
class Product(models.Model):
    CATEGORY_CHOICES = [
        ('clothing', 'Clothing'),
        ('accessories', 'Accessories'),
        ('shoes', 'Shoes'),
        ('skills', 'Skills'),
        ('superDuperUltraRareUnique Item', 'SuperDuperUltraRareUnique Item'),
    ]
    
    id = models.CharField(max_length=100, primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100, unique=True)
    price = models.IntegerField()
    description = models.TextField()
    thumbnail = models.URLField(blank=True, null=True)
    thumbnail_custom = models.ImageField(upload_to='uploads/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    is_featured = models.BooleanField(default=False)
    item_views = models.PositiveIntegerField(default=0)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    
    def __str__(self):
        return self.name

    @property
    def is_item_hot(self):
        return self.item_views > 20
            
    def increment_views(self):
        self.item_views += 1
        self.save()
        
    def choose_one(self):
        if self.thumbnail and self.thumbnail_custom:
            raise ValidationError("Choose url image or local image")
        if not self.thumbnail and not self.thumbnail_custom:
            raise ValidationError("You need to upload an image")
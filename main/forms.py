from django.forms import ModelForm
from main.models import Product

class Item_Form(ModelForm):
    class Meta:
        model = Product
        fields = ["name", "price", "description", "category", "thumbnail", "thumbnail_custom", "is_featured"]
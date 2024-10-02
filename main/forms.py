from django import forms
from django.forms import ModelForm
from main.models import Product

class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ["name", "price", "description", "stock", "image"]

    image = forms.ImageField(
        label="Image",  
        widget=forms.ClearableFileInput(attrs={"class": "form-control"})
    )
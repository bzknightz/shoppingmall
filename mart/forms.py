from django import forms
from .models import *


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = "__all__"

        widgets = {
            "name": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Product Name"}
            ),
            "price": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Product Price",
                    "type": "number",
                }
            ),
            "description": forms.Textarea(
                attrs={"class": "form-control", "placeholder": "Product Description"}
            ),
            "img": forms.FileInput(attrs={"class": "form-control"}),
        }

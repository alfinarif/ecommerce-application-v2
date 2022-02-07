from dataclasses import field
from django.forms.models import ModelForm
from store.models import (
    Category, 
    Product, 
    VariationValue, 
    Banner, 
    MyLogo, 
    MyFavicon
)


class CategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = ('__all__')
        

class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ('__all__')
        exclude = ['slug']



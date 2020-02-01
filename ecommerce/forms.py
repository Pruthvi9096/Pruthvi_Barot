from django import forms
from ecommerce.models import *
# from django.urls import reverse
# from django.utils.safestring import mark_safe
# from django.forms import widgets
from django.conf import settings

class CreateProductForm(forms.Form):
        
    name = forms.CharField(widget=forms.TextInput(
        attrs={
            "class": "form-control",
            "placeholder": "Product Name",
            "style":"width:60%;"
        })
    )
    category = forms.ModelChoiceField(queryset=Category.objects.all(),empty_label="category",widget=forms.Select(
        attrs={
            "class":"custom-select mr-sm-2",
            "style":"width:55%;"
        }))
    preview_text = forms.CharField(widget=forms.Textarea(
        attrs={
            "class": "form-control",
            "placeholder": "Preview Text",
            "style":"width:60%;height:10%;"
        })
    )
    detail_text = forms.CharField(widget=forms.Textarea(
        attrs={
            "class": "form-control",
            "placeholder": "Detail Text",
            "style":"width:60%;height:10%;"
        })
    )
    price = forms.FloatField(required=False, max_value=100000, min_value=0, 
    widget=forms.NumberInput(
        attrs={
        'class': "form-control",
        'id': 'form_homework',
         'step': "100",
         "style":"width:60%;",
         "placeholder":"Price"
         })
    ) 
    image = forms.ImageField()

class CreateCategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['category_name']

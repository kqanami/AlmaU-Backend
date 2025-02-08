from django import forms

class ProductForm(forms.Form):
    name = forms.CharField(max_length=255)
    price = forms.DecimalField(max_digits=10, decimal_places=2)

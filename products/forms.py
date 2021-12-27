from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    
    name=forms.CharField(widget=forms.TextInput(attrs={"placeholder": " Enter Product Name",}))
    price=forms.DecimalField(widget=forms.TextInput(attrs={"placeholder": " Enter Price",}))
    quantity=forms.IntegerField(widget=forms.TextInput(attrs={"placeholder": " Enter Quantity",}))    
    description=forms.CharField(widget=forms.TextInput(attrs={"placeholder": " Enter Product Description",}))
    class Meta:
        model=Product
        fields = '__all__'
        exclude = ('category',)
    
        
   
   
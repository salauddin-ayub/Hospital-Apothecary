from django import forms

from .models import Order,Product,Customer


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = '__all__'
        
       
        exclude = ('total_price',)
       
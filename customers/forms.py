from django import forms
from django.forms import ModelForm
from .models import Customer


class CustomerModelForm(ModelForm):
    
    name=forms.CharField(widget=forms.TextInput(attrs={"placeholder": " Enter Full Name",}))
    email=forms.CharField(widget=forms.TextInput(attrs={"placeholder": " Enter Email",}))
    contact=forms.CharField(widget=forms.TextInput(attrs={"placeholder": " Enter Contact",}))
   
    class Meta:
        model=Customer
        fields=['name','email','contact']



 
 
 
    
        
        
     
        

    
    
    
    
    
    
    
    
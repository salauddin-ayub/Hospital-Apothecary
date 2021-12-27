import django_filters 
from django_filters import DateFilter,CharFilter

from products.models import Product
from django.forms import DateInput

class ProductFilter(django_filters.FilterSet):
    
    name = CharFilter(field_name="name",lookup_expr='icontains')
   
    
    
    class Meta:
        model = Product
        fields = '__all__'
        exclude = ['created_at','description','category','price']
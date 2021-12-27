import django_filters 
from django_filters import DateFilter,CharFilter
from customers.models import Customer



class CustomerFilter(django_filters.FilterSet):
    name = CharFilter(field_name="name",lookup_expr='icontains')
    
    class Meta:
        model = Customer
        fields = ('name',)
       
       
       


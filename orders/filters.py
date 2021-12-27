
import django_filters 
from django_filters import DateFilter,CharFilter
from orders.models import Order

from customers.models import Customer


class OrderFilter(django_filters.FilterSet):
    status = CharFilter(field_name="status",lookup_expr="icontains")
    
    
    class Meta:
        model = Order
        fields = ['status']
        
       
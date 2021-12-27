from django.db import models

from customers.models import Customer
from products.models import Product

class Order(models.Model):
    status=(
        ('Pending','Pending'),
        ('Delivered','Delivered'),
        ('Out for delivery','out for delivery')   
    )
    
    customer=models.ForeignKey(Customer,null=True,on_delete=models.SET_NULL)
    product=models.ForeignKey(Product,null=True,on_delete=models.SET_NULL)

    
    created_at=models.DateTimeField(max_length=50,null=True,auto_now=True)
    status=models.CharField(max_length=100,null=True,choices=status)
    quantity = models.IntegerField(default=1,blank=False)

    class Meta:
        db_table = 'tbl_orders'
    
    
    def save(self,*args,**kwargs):
    	super().save(*args,**kwargs)
   
    
    
@property
def get_total_item_price(self):
    return self.quantity * self.product.price
    

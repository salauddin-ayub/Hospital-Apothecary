from django.db import models
import datetime

class Product(models.Model):
    
    category=(
                 ('indoor service','indoor service'),
                 ('outdoor service','outdoor service')
              )
   
    PRICE_UNITS_CHOICES = (
        ('', 'Choose Product Unit'),
        ('l','litre'),
        ('pcs','pcs'),
        ('gm','gm'),
        ('ml', 'ml'),
      
     
    )
    name=models.CharField(max_length=50,null=True)
    price=models.DecimalField(max_digits=20,decimal_places=2)
    quantity = models.IntegerField(blank=False,default=1)
    unit = models.CharField(max_length= 50,choices = PRICE_UNITS_CHOICES,default='')
    # slug = models.SlugField(max_length=80,default=False)
    category=models.CharField(max_length=200,null=True,choices=category)
    description=models.CharField(max_length=50,null=True)
    created_at=models.DateTimeField(auto_now=True,null=True)
   
   
    def __str__(self):
        return self.name
    class Meta:
        db_table = 'tbl_products'
    def save(self,*args,**kwargs):
    	super().save(*args,**kwargs)

class HistConf(models.Model):
	item = models.ForeignKey(Product, on_delete=models.CASCADE)
	actual= models.PositiveSmallIntegerField() 
	transition = models.IntegerField()
	total = models.PositiveSmallIntegerField()
	user = models.CharField(max_length=50)
	time = models.DateTimeField(auto_now=True,null=True)

	@classmethod
	def create(cls, actual, transition, pid, user=''):
		hist = cls(actual=actual, transition=transition, total=actual+transition, user=user, time=datetime.datetime.now(), item=pid)
		return hist

	def __str__(self):
		return f"Before: {self.actual} Change: {self.transition} After: {self.total} by user: {self.user} at {self.time}"



    
  


from django.shortcuts import render,redirect,get_object_or_404
from django.http import request,JsonResponse
from django.core import serializers

from customers.models import Customer
from orders.models import Order
from products.models import Product

from django.contrib import messages
from customers.forms import CustomerModelForm
from customers.filters import CustomerFilter
from django.contrib import messages
from django.utils import timezone
from django.views.generic import ListView,DetailView
from django.views.generic import View
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from django.template.loader import render_to_string

from django.db.models import Q
from django.contrib.auth.decorators import login_required

@login_required(login_url = '/user/login/')     
def index(request):
	form = CustomerModelForm()
	customers=Customer.objects.all().order_by("-id")
	myFilter = CustomerFilter(request.GET,queryset=customers)
	customers = myFilter.qs
	
	customer_count = customers.count()
	  

	   
	page = request.GET.get('page', 1)
	paginator = Paginator(customers, 10)
  
	try:
		customers = paginator.page(page)
	except PageNotAnInteger:
		customers = paginator.page(1)
	except EmptyPage:
		customers = paginator.page(paginator.num_pages)

	

	context={
		'customers':customers,
  		
    	'myFilter':myFilter,
		'form':form,'page':page,
		'customer_count':customer_count,
		'start': customers.start_index(),
		'end': customers.end_index(),
		}
	return render(request,'customers/copindex.html',context)

def search(request):
	data = dict()
	field_value = request.GET.get('query')
	print(field_value)
	
	if field_value:
		customers = Customer.objects.filter(
	  
											Q(name__contains=field_value)
										   |Q(email__icontains=field_value) 
										   | Q(contact__contains=field_value)  
										   |Q(date_created__contains=field_value)                      
										   )
	
		context = {'customers': customers}
		data['html_list'] = render_to_string('customers/get_search_customers.html',context,request=request)
		return JsonResponse(data)
	else:
		customers = Customer.objects.all()
		context = {'customers': customers}
		data['html_list'] = render_to_string('customers/get_search_customers.html',context,request=request)
		return JsonResponse(data)

def create(request):    
	if request.method=="POST":
		form=CustomerModelForm(request.POST)
		if form.is_valid():
			cid =request.POST['cusid']
			name=request.POST.get("name")
			email=request.POST.get("email")
			contact=request.POST.get("contact")
		  
			
			if(cid==''):
				customer=Customer(name=name,email=email,contact=contact)
			else:
				customer=Customer(id = cid,name=name,email=email,contact=contact)
				
			customer.save()
			prod=Customer.objects.values()
			# print(prod,"--------------------------")
			customer_data =list(prod)
			
			return JsonResponse({'status':'Save','customer_data':customer_data,'message':'Customer is successfully submitted'},safe=False)
		else:
			return JsonResponse({'status':0},safe=False)
	   
  
def edit(request):
    if request.method=="POST":
        id=request.POST.get('cid')
        print(id)
        customer=Customer.objects.get(pk=id)
        customer_data={"id":customer.id,"name":customer.name,"email":customer.email, "contact":customer.contact}
	
        return JsonResponse(customer_data,safe=False)


def delete(request):
    if request.method=="POST":
        id=request.POST.get('cid')
        pi=Customer.objects.get(pk=id)
        pi.delete()
	  
        return JsonResponse({'status':1,'message':'Customer is successfully deleted'},safe=False)
    else:
        return JsonResponse({'status':0,'message':'Failed to delete data'},safe=False) 

   
def cus_ord_view(request, cid):
	customer = get_object_or_404(Customer,pk=cid) 
	orders = customer.order_set.all()
	order_count = orders.count()
	order_count = orders.count()    
	customer_total_order_price=0.00
	
	for order in customer.order_set.all():
		per_total_price = float(order.product.price) * order.quantity
		customer_total_order_price += per_total_price
		
	context = {'customer_total_price':customer_total_order_price,'customers':customer, 'orders':orders, 'order_count':order_count,'order_num':order_count}
	return render(request,'customers/orderview.html',context)

	
	
	
	
 


	
	

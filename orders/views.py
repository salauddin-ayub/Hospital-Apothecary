from django.shortcuts import render,redirect,get_object_or_404,reverse

from django.http import JsonResponse
from .models import Order,Customer,Product
from orders.forms import OrderForm
from orders.filters import OrderFilter
from django.forms import inlineformset_factory
from django.contrib import messages

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from django.db.models import Q

from django.template.loader import render_to_string
from django.contrib.auth.decorators import login_required

from django.views.generic import View
from django.contrib.auth.mixins import LoginRequiredMixin


def create(request,cid):
    
    OrderFormSet = inlineformset_factory(Customer,Order,fields='__all__',exclude=('total_price',),extra=5) 
    cus = Customer.objects.get(pk=cid)
    formset = OrderFormSet(queryset=Order.objects.none(),instance=cus)
    if request.method=='POST':
        formset = OrderFormSet(request.POST,instance = cus)
        if formset.is_valid():
            formset.save()
        messages.success(request,"Order is successfully added",extra_tags = 'alert')
        return redirect('customer_app:view', cid)
    
    return render(request,'orders/create.html',{'formset':formset,'customer':cus})





@login_required(login_url='/user/login/')
def index(request):
    orders=Order.objects.all().order_by("-id")
    total_orders=orders.count()
    pending=orders.filter(status='Pending').count()
    delivered=orders.filter(status="Delivered").count()
    orders = pagination(request,orders)
         
    context={
        'orders':orders,'total_orders':total_orders,
        'orders_pending':pending,'orders_delivered':delivered,
        'start':orders.start_index(),
        'end':orders.end_index()
        
        }
    return render(request,'orders/index.html',context)


        
    


def pagination(request,object):
    page = request.GET.get('page', 1)
    paginator = Paginator(object, 5)
  
    try:
        orders = paginator.page(page)
    except PageNotAnInteger:
        orders = paginator.page(1)
    except EmptyPage:
     
        orders = paginator.page(paginator.num_pages)
        
    return orders

    
def search(request):
    data = dict()
    field_value = request.GET.get('query')
    print(field_value)
    
    if field_value:
        orders = Order.objects.filter(
                                            Q(product__name__contains=field_value)
                                           |Q(status__icontains=field_value) 
                                        
                                           | Q(quantity__contains=field_value)
                                            | Q(customer__name__contains=field_value)
                                           )
        context = {'orders': orders}
            
        data['html_list'] = render_to_string('orders/get_search_orders.html',context,request=request)
        return JsonResponse(data)
    

    else:
        orders = Order.objects.all()
       
        context = {'orders': orders}
        data['html_list'] = render_to_string('orders/get_search_orders.html',context,request=request)
        return JsonResponse(data)


def edit(request, cid, oid):    
    ord = get_object_or_404(Order,pk = oid)
    customer = get_object_or_404(Customer,pk=cid)
    form=OrderForm(instance=ord)
    
    
    if(request.method=='POST'):
        
        form=OrderForm(request.POST,instance=ord)
        if(form.is_valid()):
            form.save()
            messages.success(request,'Order is successfully updates.',extra_tags='alert')
            
            return redirect('customer_app:view', cid)
    return render(request,'orders/update.html',{'form':form,'customer_record':customer})


def delete(request, oid):
    ord = get_object_or_404(Order,pk = oid) 
    
    if request.method=='POST':
        ord.delete()  
        return redirect('order_app:list')
    
    return render(request,'orders/delete.html',{'orders':ord})



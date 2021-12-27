from django.shortcuts import render,redirect,get_object_or_404

from django.http import request,JsonResponse
from django.template.loader import render_to_string

from orders.models import Order
from products.models import Product
from customers.models import Customer
from .forms import ProductForm
from django.contrib import messages
from .filters import ProductFilter

from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q,Sum
from django.contrib.auth.decorators import login_required

@login_required(login_url = '/user/login/')
def index(request):   
    form = ProductForm()
    products=Product.objects.all()
    product_count = products.count()
    products = getPaginator(request,products)

    context={'products':products,
           
           
             'form':form,
             'start':products.start_index(),
             'end':products.end_index(),
             'products_count':product_count
             }
    return render(request,'products/index.html',context)



def getPaginator(request,object):
    page = request.GET.get('page', 1)
    paginator = Paginator(object, 5)
  
    try:
        products = paginator.page(page)
        
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)
        
    return products


    
def search(request):
    data = dict()
    field_value = request.GET.get('query')
    print(field_value)
    
    if field_value:
        products = Product.objects.filter(
                                            Q(name__icontains=field_value)
                                           | Q(price__icontains=field_value) 
                                           | Q(description__icontains=field_value)
                                           | Q(quantity__icontains=field_value)
                                           | Q(id__icontains=field_value)
                                           | Q(category__icontains=field_value)
                                           |Q(created_at__contains=field_value)
                                           )

        context = {'products': products}
        data['html_list'] = render_to_string('products/get_search_products.html',context,request=request)
        return JsonResponse(data,safe=False)

    else:
        products = Product.objects.all()
        context = {'products': products}
        data['html_list'] = render_to_string('products/get_search_products.html',context,request=request)
        return JsonResponse(data)



def create(request): 
   
    if request.method=="POST":
        form=ProductForm(request.POST)
        if form.is_valid():
            pid =request.POST["proid"]
            name=request.POST.get("name")
            price=request.POST.get("price")
            quantity=request.POST.get("quantity")
            unit=request.POST.get("unit")
            description=request.POST.get("description")
            
            if(pid==''):
                product=Product(name=name,price=price,quantity=quantity,unit=unit,description=description)
                
            else:
                product=Product(id = pid,name=name,price=price,quantity=quantity,unit=unit,description=description)
                
            product.save()
            prod=Product.objects.values()
            product_data =list(prod)
            return JsonResponse({'status':'Save','product_data':product_data,'message':'Product is successfully submitted'},safe=False)
        else:
            return JsonResponse({'status':0})
       
  

    
    
def edit(request):
    print("edit is click ----------------------")
    if request.method=="POST":
        id=request.POST.get('pid')
        product=Product.objects.get(pk=id)
        product_data={"id":product.id,"name":product.name,"price":product.price,
                      "quantity":product.quantity,"unit":product.unit,"description":product.description}
    
        return JsonResponse(product_data)
    
    
    
    
def delete(request):
    if request.method=="POST":
        id=request.POST.get('pid')
        pi=Product.objects.get(pk=id)
        pi.delete()
      
        return JsonResponse({'status':1,'message':'Product is successfully deleted'},safe=False)
    else:
        return JsonResponse({'status':0,'message':'Failed to delete data'},safe=False)    




def productData(request,cid):
    
    productData = []
    cus = Customer.objects.get(pk=cid)
    order = cus.order_set.all()
   
    for i in order:
        productData.append({i.customer.name:i.product.price})
        
    print(productData)
    return JsonResponse(productData,safe=False)









# ------------------------------------------------------------------------------------------------------------------------------------
'''

def delete(request, pid):
 # cus=Customer.objects.get(id=pk)
    pro = get_object_or_404(Product,pk = pid)
    
                                     # print(f'I am instance of {{cus}}')
   
    if request.method=='POST':  #if i confirm in delete.html page otherwise dont need post request
        pro.delete()   #grab customer details and delete and after deleting moves to /customers/list/
     
        return redirect('product_app:list')
    
    return render(request,'products/delete.html',{'name':pro })#urls.py ko url render ma url search garxa at first




def edit(request, pid):    
    # pro=Product.objects.get(id=pk) #i get all value and show that value to next page
    pro = get_object_or_404(Product,pk = pid)
    form=ProductForm(instance=pro)
    
    if(request.method=='POST'):
        
        form=ProductForm(request.POST,instance=pro)
        if(form.is_valid()):
            form.save()
            messages.success(request,'Product is successfully updated.',extra_tags='alert')
            
        return redirect('product_app:list')#maila update.html ko save garda or post ma jada yo url ma redirect hunxa

    # else:
    #     form = ProductForm()
        
  
    return render(request,'products/update.html',{'form':form})
    
    '''
    
    
    









    
    
    




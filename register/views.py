from django.shortcuts import render,redirect
from django.contrib.auth.views import LoginView,LogoutView
from django.conf import settings
from django.views.generic import CreateView
from .forms import SignupForm,LoginForm,UpdateDefaultProfile,UpdateCustomProfile
from django.contrib import messages

from customers.models import Customer
from django.contrib import messages
from orders.models import Order
from products.models import Product,HistConf
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from django.http import HttpResponse, HttpResponseRedirect
from .decorators import unauthenticated_user, allowed_users, admin_only
import json

from django.views.generic import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from register.filters import CustomerFilter

from datetime import datetime, timedelta

# Create your views here.
def first_page(request):
	current_date = datetime.now()
	return render(request,'registers/firstpage.html',{'current_date':current_date})

@login_required(login_url='/user/login/')
def dashboard(request):
	customers=Customer.objects.all()
	total_customers=customers.count()
	orders=Order.objects.all()

	total_orders=orders.count()
	products = Product.objects.all()
	total_products = products.count()	
	pending=orders.filter(status='Pending').count()
	delivered=orders.filter(status="Delivered").count()
 
 
	myFilter = CustomerFilter(request.GET, queryset=customers)
	customers = myFilter.qs 
	today_customers = customers.filter(date_created__gte = datetime.now() - timedelta(days=1)).count()
	today_order = orders.filter(created_at__gte = datetime.now() - timedelta(days=1))

	order_total_price=0.00
 
	# for order in today_order:
	# 	per_total_price = float(order.product.price) * order.quantity
	# 	order_total_price += per_total_price
	# print(order_total_price)
	
	context={
			'customers':customers,'orders_total_price':order_total_price,'total_orders':total_orders,
   			'myFilter':myFilter,'today_customers':today_customers,'current_data':datetime.now(),
			'orders_pending':pending,'orders_delivered':delivered,'total_products':total_products,'total_customers':total_customers
			}
	
	return render(request,'registers/index.html',context)

@unauthenticated_user
def loginPage(request):
	form = LoginForm()

	if request.method == 'POST':
		username = request.POST.get('username')
		password =request.POST.get('password')
		email =request.POST.get('email')
		user = authenticate(request,email=email, username=username, password=password)
		if user is not None:
			login(request, user)
			return redirect('home')
		else:
			messages.error(request, 'Username OR password is incorrect')

	context = {'form':form}
	return render(request, 'registers/login.html', context)
	
@unauthenticated_user
def SignupView(request):

	form = SignupForm()
 
	if request.method == 'POST':
		form = SignupForm(request.POST)
		if form.is_valid():
			user = form.save()
			username = form.cleaned_data.get('username')
			group = Group.objects.get(name='employee')
			user.groups.add(group)
			print("--------------",user)
			messages.success(request, 'Account was created for ' + username)
			return redirect('register_app:login')
		
	context = {'form':form}
	return render(request, 'registers/register.html', context)


class UserLogout(LogoutView):
	pass


from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm


def UserProfile(request):
	defaultForm = UpdateDefaultProfile(instance=request.user)
	customForm = UpdateCustomProfile(instance=request.user.profile)
	PassForm = PasswordChangeForm(request.user)
	
	if request.method == 'POST' and 'profile_edit' in request.POST:
		defaultForm = UpdateDefaultProfile(request.POST,instance=request.user)
		customForm = UpdateCustomProfile(request.POST,request.FILES,instance=request.user.profile)
  
		if defaultForm.is_valid() and customForm.is_valid():
			defaultForm.save()
			customForm.save()
		
			messages.success(request,"Your record is successfully updated")
			return redirect('register_app:user_view')


	if request.method == 'POST' and 'change_pass_button' in request.POST:
		
		PassForm = PasswordChangeForm(user = request.user,data = request.POST)
  
		if PassForm.is_valid():
			PassForm.save()
			update_session_auth_hash(request, PassForm.user) 
			messages.success(request,"Your password is successfully updated")
			return redirect('register_app:user_view')
		
	return render(request,'registers/edit_user.html',{'defaultForm':defaultForm,'customForm':customForm,'PassForm':PassForm})

	








from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static

from register import views
from django.contrib.auth import views as auth_views
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.first_page,name="home"),
    # path('user/',include('register.urls', namespace ='register_app')),
    path('dashboard/',views.dashboard,name="dashboard"),

    # path('customers/',include('customers.urls', namespace="customer_app")),
	# path('products/',include('products.urls', namespace="product_app")),
	# path('orders/',include('orders.urls', namespace="order_app")),
    path('donorreg/',include(('dreg.urls', 'dregsite'), namespace='dregsite')),
    path('user/',include(('register.urls', 'register_app'), namespace='register_app')),
    path('customers/',include(('customers.urls', 'customer_app'), namespace='customer_app')),
    path('products/',include(('products.urls', 'product_app'), namespace='product_app')),
    path('orders/',include(('orders.urls', 'order_app'), namespace='order_app')),
    path('reset_password/',auth_views.PasswordResetView.as_view(template_name = 'passwordreset/password_reset_email.html'), 
		 name = "password_reset"),
	
	path('reset_password_sent/',auth_views.PasswordResetDoneView.as_view(template_name = 'passwordreset/password_reset_sent.html'), 
		 name = "password_reset_done"),
	
	path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name='passwordreset/password_reset_form.html'),
		 name="password_reset_confirm"),  

	path('reset_password_complete/',auth_views.PasswordResetCompleteView.as_view(template_name='passwordreset/password_reset_complete.html'),
		 name="password_reset_complete"),
   
]
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)







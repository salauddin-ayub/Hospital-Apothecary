from django.urls import path
from .views import searchdisplay, donorlistdetail

urlpatterns = [
    path('', searchdisplay, name='searchsite1'),
    path('donorlist/', searchdisplay, name='donorlistsite'),
    path('donorlist/donorlistdetail/<email>/', donorlistdetail, name='donorlistdetailsite'),
]
from django.urls import path
from register import views
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import PasswordResetDoneView

#app_name = 'register_app'

urlpatterns = [
    path('login/',views.loginPage,name="login"),
    path('register/',views.SignupView,name="register"),
    path('logout/',views.UserLogout.as_view(),name="logout"),
    path('profile/',views.UserProfile,name="user_view"),
    
]

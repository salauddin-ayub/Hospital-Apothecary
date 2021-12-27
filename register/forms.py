from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,PasswordResetForm,AuthenticationForm

from django import forms
from django.forms import EmailField,TextInput,PasswordInput,ImageField
from .models import Profile



from django.utils.translation import gettext_lazy as _

class LoginForm(AuthenticationForm):
    pass

class SignupForm(UserCreationForm):
	username=forms.CharField(widget=forms.TextInput(attrs={"placeholder": " Enter Username",}))
	email=forms.EmailField(widget=forms.TextInput(attrs={"placeholder": " Enter Email",}))
	password1=forms.CharField(widget=forms.TextInput(attrs={"placeholder": " Enter Password",'type' : 'password'}),label=_("Password"))
	password2=forms.CharField(widget=forms.TextInput(attrs={"placeholder": " Confirm Password",'type' : 'password'}),label=_("Confirm Password"))
	

	
	class Meta:
		model = User
		fields = ('username','email','password1','password2',)
		help_texts= {
			'username':None,
		}



class UpdateDefaultProfile(forms.ModelForm):
	email=forms.EmailField(widget=forms.TextInput(attrs={"placeholder": " Enter Email",}))
	class Meta:
		model = User
		fields = ('username','email',)


class UpdateCustomProfile(forms.ModelForm):
   	
	class Meta:
		model = Profile
		fields = ('fname','lname','address','contact','profile_img',)
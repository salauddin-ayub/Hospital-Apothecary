from django.shortcuts import render
from .forms import DonorRegistration
from .models import DonorList


#Donnor forms display
def donorregdisplay(request):
    forms = DonorRegistration()
    if request.method == 'POST':
        forms = DonorRegistration(request.POST)
        if forms.is_valid():
            forms.save()
            print(forms.errors)
            context_details ={
                'forms' : forms
            }
            #After donor registation donor details display
            return render(request, 'donor_reg_s.html', context_details)

    context = {
                'forms' : forms,
            }


    return render(request, 'donor_reg.html', context)

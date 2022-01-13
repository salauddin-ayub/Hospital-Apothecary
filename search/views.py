from django.shortcuts import render
from .forms import DonorSearch
from dreg .models import DonorList
from .models import SearchLogo

# Create your views here.
def searchdisplay(request):
    search_forms = DonorSearch()
 
    if request.method == 'POST':
        search_forms = DonorSearch(request.POST)
        if search_forms.is_valid():
            blood_group = search_forms.cleaned_data['select_blood_group']
            location = search_forms.cleaned_data['select_location']
            donor_filter = DonorList.objects.filter(blood_group=blood_group, home_address__icontains=location)
            context = {
                'donor_filter' : donor_filter
            }
            return render(request, 'donor_list.html', context)

    context = {
        'forms_search' : search_forms,
        
    }   
    return render(request, 'donor_search.html', context)

def donorlistdetail(request, email):
    email = email
    detail = DonorList()
    detail = DonorList.objects.get(email=email)
    context = {
        'details' : detail
    }
    return render(request, 'donor_l_d.html', context)

from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import View
from django.views.generic import CreateView
from django.contrib import messages
from django.db.models import Q
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.forms import UserCreationForm
from .models import *
from .forms import *
import folium
import geocoder


#Create your views here.
def home(request):
    return render(request, "app/home.html" )

def CarSelector(request):
    return render(request, "app/selectcar.html" )

def booking(request):
    return render(request, "app/booking.html" )

def about(request):
    return render(request, "app/about.html" )

def contact(request):
    return render(request, "app/contact.html" )


class CustomerRegistrationForm(View):
    def get(self, request):
        form = RegisterCustomerForm()
        return render(request, 'app/customerregistration.html', {'form':form})
    def post(self, request):
        form = RegisterCustomerForm(request.POST)
        if form.is_valid():
            messages.success(request, 'Congratulation!! Sucessfully Registered')
            form.save()
        return render(request, 'app/customerregistration.html', {'form':form})


@method_decorator(login_required, name='dispatch')
class ProfileView(View):
    def get(self, request):
        form = CustomerProfileForm()
        return render(request, 'app/cprofile.html', {'form':form, 'active':'btn-primary'})
    def post(self, request):
        form = CustomerProfileForm(request.POST)
        if form.is_valid(): 
            usr = request.user
            name = form.cleaned_data['name']
            locality = form.cleaned_data['locality']
            city = form.cleaned_data['city']
            state = form.cleaned_data['state']
            zipcode = form.cleaned_data['zipcode']
            reg = Customer(user=usr, name=name, locality=locality, city=city, state=state, zipcode=zipcode)
            reg.save()
            messages.success(request, 'Congratulations!! Profile Updated Sucessfully')
        return render(request, 'app/cprofile.html', {'form':form, 'active':'btn-primary'})

@login_required
def changePassword(request):
    return render(request, "app/changepassword.html" )



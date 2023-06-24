from django.shortcuts import render
from django.views import View
#import models/DB from models.py
from .models import Customer, Product, Cart, OrderPlaced
#import forms for Registration
from .forms import CustomerRegistrationForm
#to show message
from django.contrib import messages

# Create your views here.
#product sliding
class ProductView(View):
    def get(self, request):
        ebook = Product.objects.filter(category = 'EB')
        hoverboard = Product.objects.filter(category = 'HB')
        smartphone = Product.objects.filter(category = 'SP')
        actioncamera = Product.objects.filter(category = 'AC')
        virtualreality = Product.objects.filter(category = 'VR')

        return render(request, 'Shop/home.html', {'ebook' : ebook,
                    'hoverboard' : hoverboard, 'smartphone' : smartphone, 
                    'actioncamera' : actioncamera, 'virtualreality' : virtualreality})

#product page
class ProductDetailView(View):
    def get(self, request, pk):
        products = Product.objects.get(pk = pk)
        return render(request, 'Shop/productdetails.html', {'products' : products})
#brandwise product for action camera

def actioncamera(request, data = None):
    #for no data and model: Product and variable names are from that model(category, brand, discounted_price)
    if data == None:
        actioncameras = Product.objects.filter(category = 'AC') 

    elif data == 'GoPro' or data == 'Ricoh-Theta-Z1' or data == 'Xiaomi':
        actioncameras = Product.objects.filter(category = 'AC').filter(brand = data)
    elif data == 'below':
        actioncameras = Product.objects.filter(category = 'AC').filter(discounted_price <= 25000)
    elif data == 'above':
        actioncameras = Product.objects.filter(category = 'AC').filter(discounted_price > 25000)

    return render(request, 'Shop/actioncamera.html', {'actioncameras': actioncameras})
    
    
#forms.py: CustomerRegistrationForm
#create view for Registraion Class 
class CustomerRegistrationView(View):
    #self: to call attributes
    def get(self,request):
        form = CustomerRegistrationForm()
        return render(request, 'Shop/customerregistration.html',{'form' : form})
    
    #create POST method not to show the user details on url
    def post(self,request):
        form = CustomerRegistrationForm(request.POST)
        #check validation
        if form.is_valid():
            # to generate message after registration 
            messages.success(request,"Registred Successfully")
            # save the data in DB
            form.save()
        return render(request, 'Shop/customerregistration.html',{'form' : form})
        #else form will not save
    

def profile(request):
    return render(request, 'Shop/profile.html' )

def address(request):
    return render(request, 'Shop/address.html')





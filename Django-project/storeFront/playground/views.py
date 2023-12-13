from django.shortcuts import render
from django.http import HttpResponse
from .models import Member
from .models import Product
from .forms import MemberForm
from .forms import ProductForm

# dummy class for debugger preactice
def calculate():
    x = 1 
    y = 2
    return x

def say_hello(request):
    # In this func, in real life, we can pull data from db, transform data,
    # send emails etc.
    x = calculate() # create breakpoint for debugging
    return render(request, 'playground/hello.html', { 'name': 'Saif'}) # using render func to send req and return template as response

# home func pull the data from database and show at homescreen
def home(request):
    all_members = Member.objects.all # taking all member's objects in all_members var
    all_products = Product.objects.all
    return render(request, 'playground/home.html', 
                  {
                      'all_items': all_members,
                      'all_products': all_products,
                  }
            ) # taking all in all_items. all_items is a var which will be used in home.html 

# for data entry to Product database
def join(request):
    if request.method == "POST":
        form = MemberForm(request.POST or None)
        if form.is_valid():
            form.save()
        return render(request, 'playground/join.html', {})
    else:
        return render(request, 'playground/join.html', {})

# for data entry to Product database
def product_entry(request):
    if request.method == "POST": # if req method is POST take ProductForm data into the form or take none.
        form = ProductForm(request.POST or None)
        if form.is_valid(): 
            form.save()   # check the validity of form. save if valid
        return render(request, 'playground/product_entry.html', {})  # return to product_entry.html page after saving
    else:    
        return render(request, 'playground/product_entry.html') # if there is no POST req, return to the form.
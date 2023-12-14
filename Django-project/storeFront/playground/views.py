from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Member
from .models import Product
from .forms import MemberForm
from .forms import ProductForm
from django.contrib import messages

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
        # check if form has all input field filled up
        if form.is_valid():
            form.save() # form will be saved in db
        else:
            fname = request.POST['fname'] # it wll make stay the value in input field
            lname = request.POST['lname'] # when page is rendered. give value to the dictionary
            email = request.POST['email'] # of render function
            password = request.POST['password']
            age = request.POST['age']

            messages.success(request, 'There was an error in your form! Please try again.')
            return render(request, 'playground/join.html', 
                          {
                              'fname': fname,
                              'lname': lname,
                              'email': email,
                              'password': password,
                              'age': age,
                          } # it wll make stay the value in input field
                          )
        # allert message for confirmation
        messages.success(request, 'Your form has been submitted successfully!')
        return redirect('show_memberdb')
    else:
        return render(request, 'playground/join.html', {})



# for data entry to Product database
def product_entry(request):
    if request.method == "POST": # if req method is POST take ProductForm data into the form or take none.
        form = ProductForm(request.POST or None)
        # check if form has all input field filled up
        if form.is_valid(): 
            form.save()   # check the validity of form. save if valid
        else:
            # picking the values from input field by POST method
            name = request.POST['name']
            description = request.POST['description']
            stock = request.POST['stock']
            category = request.POST['category']
            price = request.POST['price']
            company = request.POST['company']

            messages.success(request, 'There was an error in your form! Please try again.')
            return render(request, 'playground/product_entry.html', 
                          { # enter the values from picked up var to dictionary var 'dic_var': picked_var
                              'name': name,
                              'description': description,
                              'stock': stock,
                              'category': category,
                              'price': price,
                              'company': company,
                          }
                          )
        # allert message for confirmation
        messages.success(request, 'Your form has been submitted successfully!')
        return redirect('show_productdb')  # show success and product db page after submitting
    else:    
        return render(request, 'playground/product_entry.html') # if there is no POST req, return to the form.
    


# show databases after redirected from form. Confirm that form has been submitted.
def show_memberdb(request):
    all_members = Member.objects.all # taking all member's objects in all_members var
    return render(request, 'playground/show_memberdb.html',
                  {
                      'all_items': all_members,
                  }
            ) # taking all in all_items. all_items is a var which will be used in show_result.html


# show databases after redirected from form. Confirm that form has been submitted.
def show_productdb(request):
    all_products = Product.objects.all
    return render(request, 'playground/show_productdb.html', 
                  {
                      'all_products': all_products,
                  }
            ) # taking all in all_items. all_items is a var which will be used in home.html 
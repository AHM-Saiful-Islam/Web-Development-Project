from django.shortcuts import render
from django.http import HttpResponse

# dummy class for debugger preactice
def calculate():
    x = 1 
    y = 2
    return x

def say_hello(request):
    # In this func, in real life, we can pull data from db, transform data,
    # send emails etc.
    x = calculate() # create breakpoint for debugging
    return render(request, 'hello.html', { 'name': 'Saif'}) # using render func to send req and return template as response

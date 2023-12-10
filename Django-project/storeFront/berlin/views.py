from django.utils import timezone
from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, "berlin/home.html")

def about(request):
    return render(request, "berlin/about.html")

def contact(request):
    return render(request, "berlin/contact.html")

def hello_there(request):
    # we can use variables also.
    # dates = timezone.now()
    # template = 'berlin/hello_there.html'
    return render(
        request,
        'berlin/hello_there.html',
        {
            'name': 'Saif',
            'date': timezone.now(),
        }
    )
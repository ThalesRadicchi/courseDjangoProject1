from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, "recipes/home.html", context={
        'name': 'Thales Radicchi'
    })

def about(request):
    return HttpResponse('ABOUT 2')

def contact(request):
    return render(request, 'me-apague/temp.html')
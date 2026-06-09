from django.shortcuts import render
from django.http import HttpResponse
from .models import *

def index(request):
    return render(request, 'index.html')

def service(request):
    return render(request, 'service.html')

def about(request):
    return render(request, 'about.html')

def resource(request):
    return render(request, 'resource.html')

def join(request):
    return render(request, 'join-our-team.html')

def project(request):
    return render(request, 'project.html')

def faq(request):
    return render(request, 'faq.html')

def contact(request):
    return render(request, 'contact.html')
# Create your views here.


from django.shortcuts import render
from .models import Service
# Create your views here.

def services(request):
    services = Service.objects.filter(status = True)
    context = {
        'services':services,
    }
    return render(request,'services/services.html',context=context)

def service_details(request):
    return render(request,'services/service-details.html')

def blogs(request):
    return render(request,'services/blog.html')

def blog_details(request):
    return render(request,'services/blog-details.html')

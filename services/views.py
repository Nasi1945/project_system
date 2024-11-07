from django.shortcuts import render

# Create your views here.

def services(request):
    return render(request,'services/services.html')

def service_details(request):
    return render(request,'services/service-details.html')

def blogs(request):
    return render(request,'services/blog.html')

def blog_details(request):
    return render(request,'services/blog-details.html')

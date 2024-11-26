from django.shortcuts import render
from .models import Staff
def home(request):
    return render(request,'root/index.html')

def about(request):
    staffs = Staff.objects.filter(status = True)
    context = {
        'staffs':staffs,
    }
    return render (request,'root/about.html',context=context)

def contact(request):
    return render (request,'root/contact.html')


from django.shortcuts import render
from .models import Books,Genre,Comment,Reply
# Create your views here.
def book(request):
    books = Books.objects.filter(status = True)
    context = {
        'books' : books,
    }
    return render(request,'books/book.html',context=context)

def book_details(request):
    b_details = Books.objects.filter(status = True)
    return render(request,'books/book-details.html')

def lib_comments(request):
    return render(request,'books/lib-comments.html')

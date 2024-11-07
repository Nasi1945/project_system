from django.shortcuts import render

# Create your views here.
def book(request):
    return render(request,'books/book.html')

def book_details(request):
    return render(request,'books/book-details.html')

def lib_comments(request):
    return render(request,'books/lib-comments.html')

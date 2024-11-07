from django.urls import path
from .views import lib_comments,book,book_details

app_name = 'books'

urlpatterns = [
    path('',book,name='book'),
    path('details',book_details,name='book_details'),
    path('library_comments',lib_comments,name='lib_comments')
]

from django.urls import path
from .views import services,service_details,blogs,blog_details

app_name = 'services'

urlpatterns = [
    path('',services,name='service'),
    path('s_details',service_details,name='ser_details'),
    path('blog',blogs,name='blogs'),
    path('b_details',blog_details,name='blo_details'),
]

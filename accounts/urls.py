from django.urls import path
from .views import login,sign_up

app_name = 'accounts'

urlpatterns = [
    path('',login,name='loginview'),
    path('signup',sign_up,name='signup')
]


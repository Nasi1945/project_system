from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Section(models.Model):
    name = models.CharField(max_length= 100)
    created_at = models.DateTimeField(auto_now_add= True)
    updated_at = models.DateTimeField(auto_now= True)
    
    def __str__(self):
        return self.name
    
    class Mata:
        ordering = ('created_at',)
        
class Staff(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='staff',default='sstaff.jpg')
    section = models.ManyToManyField(Section)
    status = models.BooleanField(default= False)
    created_at = models.DateTimeField(auto_now_add= True)
    updated_at = models.DateTimeField(auto_now= True)
    
    def __str__(self):
        return self.user.username
    
    class Mata:
        ordering = ('created_at',)
        

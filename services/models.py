from django.db import models

# Create your models here.
class Attribute(models.Model):
    name = models.CharField(max_length=120)
    content = models.TextField(default='کمک کننده')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=False)
    
    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ('created_at',)
        
        
class service(models.Model):
    name = models.CharField(max_length=120)
    content = models.TextField(default='این سرویس کار شما را راحت تر کرده است')
    image = models.ImageField(upload_to='services', default='service.jpg')
    attribute = models.ManyToManyField(Attribute)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=False)
    
    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ('created_at',)
    
    
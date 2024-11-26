from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Genre(models.Model):
    name = models.CharField(max_length= 100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add= True)
    updated_at = models.DateTimeField(auto_now= True)
    
    def __str__(self):
        return self.name
    
    class Mata:
        ordering = ('created_at',)
    
class Books(models.Model):
    name = models.CharField(max_length= 100)
    genre = models.ManyToManyField(Genre)
    writer = models.TextField()
    likes = models.IntegerField()
    capacity = models.IntegerField()
    image = models.ImageField(upload_to='books',default='book.jpg')
    content = models.TextField(default='داستانی عالی')
    status = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add= True)
    updated_at = models.DateTimeField(auto_now= True)
    
    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ('created_at',)
    
class Comment(models.Model):
    book = models.ForeignKey(Books,on_delete=models.CASCADE)
    name = models.ForeignKey(User,on_delete=models.CASCADE)
    message = models.TextField()
    statue = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name.username
    
class Reply(models.Model):
    comment = models.ForeignKey(Comment,on_delete=models.CASCADE)
    name = models.ForeignKey(User,on_delete=models.CASCADE)
    message = models.TextField()
    statue = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name.username
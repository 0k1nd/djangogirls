from django.conf import settings
from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    image = models.ImageField(blank=True, null=True)
    video = models.FileField(blank=True, null=True)
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
    
class Item(models.Model):
    name = models.CharField(max_length=1000)
    body = models.TextField()
    date = models.DateTimeField(blank=timezone.now)
    
    def publish(self):
        self.published_date = timezone.now()
        self.save()

# Create your models here.

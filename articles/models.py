from django.db import models
from django.contrib.auth.models import User
from django import forms
import random

# Create your models here.
default_images = ['default1.png', 'default.png', 'default2.png']

class Article(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField()
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    thumb = models.ImageField(default=random.choice(default_images), blank=True)
    author = models.ForeignKey(User, default=None, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.title
    
    def snippet(self):
        return self.body[:50] + '...'

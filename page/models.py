from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.


class Team(models.Model):
    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to ='uploads/')
    designation = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Blog(models.Model):
    title = models.CharField(max_length=1000)
    img = models.ImageField(upload_to ='uploads/')
    body = RichTextUploadingField()
    video_url = models.URLField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Summer(models.Model):
    title = models.CharField(max_length=1000)
    img = models.ImageField(upload_to ='uploads/')
    body = RichTextUploadingField()
    year = models.CharField(max_length=1000, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title + ' ' +self.year


class Category(models.Model):
    name = models.CharField(max_length=30)
    image = models.ImageField(null=True, upload_to ='uploads/')
    
    
    def __str__(self):
        return self.name

    class Meta:
    	verbose_name_plural = 'Categories'

class Product(models.Model):
    name = models.CharField(max_length=100)
    upload = models.ImageField(upload_to ='uploads/')
    url = models.URLField(max_length=2000)
    button_text = models.CharField(max_length=100, default="null")
    is_active = models.BooleanField(default=True)
    category = models.ManyToManyField(Category,blank=True)
    

    def __str__(self):
        return self.name






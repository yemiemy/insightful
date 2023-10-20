from django.db import models

# Create your models here.


class Team(models.Model):
    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to ='uploads/')
    designation = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=30)
    
    
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






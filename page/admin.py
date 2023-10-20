from django.contrib import admin

# Register your models here.

from .models import Category, Product, Team, Blog

admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Team)
admin.site.register(Blog)
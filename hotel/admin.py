from django.contrib import admin
from .models import items

class Items(admin.ModelAdmin):
    list_display=('name','price','quantity')

# Register your models here.
admin.site.register(items,Items)


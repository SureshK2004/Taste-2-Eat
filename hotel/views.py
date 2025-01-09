from django.shortcuts import render
from django.http import HttpResponse
from .models import items

# Create your views here.
def home(request):
    items_list=items.objects.all()
    return render (request, 'home.html',{'items':items_list})
from django.shortcuts import render
from products.models import products

def home(request):
    posts = products.objects.all()
    return render (request, 'layout.html',{'posts':posts})
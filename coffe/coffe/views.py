from django.shortcuts import render, get_object_or_404
from products.models import products, orders

def home(request):
    posts = products.objects.all()
    return render (request, 'layout.html',{'posts':posts})
def order(request, product_id):
    product = get_object_or_404(products, id=product_id)
    return render (request, 'orders.html',{'product':product})
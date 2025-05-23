from django.shortcuts import get_object_or_404,redirect, render
from .models import orders




def update_orders(request, product_id):
    order = get_object_or_404(orders, id = product_id)
    if request.method == "POST":
        order.F_name = request.POST.get("name")
        order.M_name = request.POST.get("M_name")
        order.phone = request.POST.get("phone")
        order.email = request.POST.get("email")
        order.city = request.POST.get("addres")
        order.street = request.POST.get("street")
        order.save()
    return redirect('products:order_succ')
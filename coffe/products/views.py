from django.shortcuts import get_object_or_404,redirect, render
from .models import orders
from .models import products




def update_orders(request, product_id):
    if request.method == 'POST':
        print("Form submitted!")
        product = get_object_or_404(products, id=product_id)

        F_name = request.POST.get("name")
        M_name = request.POST.get("M_name")
        phone = request.POST.get("phone")
        email = request.POST.get("email")
        city = request.POST.get("address") 
        street = request.POST.get("street")

        order = orders(
            product=product,
            F_name=F_name,
            M_name=M_name,
            phone=phone,
            email=email,
            city=city,
            street=street
        )
        order.save()

        return redirect('orders:order_succ')
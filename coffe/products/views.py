from django.shortcuts import render, redirect,get_object_or_404
from products.models import products, orders
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.mail import EmailMessage
from django.conf import settings
from django.template.loader import render_to_string
def succ(request, order_id):
    order = get_object_or_404(orders, id=order_id)
    template = render_to_string('products/email_template.html',
                                {'name':order.F_name,
                                'item':order.product
                                })
    email = EmailMessage(
        'Your Coffee Order is Confirmed!',
        template,
        settings.EMAIL_HOST_USER,
        [order.email]
    )
    email.send()
    return render(request, 'products/success.html',{'order': order})
def update_orders(request, product_id):
    if request.method == 'POST':
        print("Form submitted!")
        product = get_object_or_404(products, id=product_id)
        F_name = request.POST.get('name')
        M_name = request.POST.get('M_name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        city = request.POST.get('address') 
        street = request.POST.get('street')

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

        return redirect('orders:successfull', order_id=order.id)
@login_required(login_url='orders:login')
def order_list(request):
    lists = orders.objects.all()
    return render(request, 'products/delivery.html', {'lists': lists})



def login_user(request):
    user_aut = False
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate (request=request, username = username, password=password)
        if user is not None:
            login(request, user)
            user_aut = True
            return redirect('orders:order_list')
        else:
            messages.error(request, '*Invalid username or password')
            return redirect('orders:login')
    return render(request, 'products/login.html')
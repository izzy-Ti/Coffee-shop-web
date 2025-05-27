
from django.contrib import admin
from django.urls import path,include
from .import views

app_name = 'orders'

urlpatterns = [
        path('order/<int:product_id>/', views.update_orders, name='update_orders'),
        path('order_list/',views.order_list, name = 'order_list')
]
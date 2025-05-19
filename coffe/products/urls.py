from django.contrib import admin
from django.urls import path
from . import views

app_name = "products"
urlpatterns = [
    path('update/<int:product_id>/', views.update_orders, name='products'),
]

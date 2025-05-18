from django.contrib import admin

# Register your models here.

from .models import products
from .models import orders
# Register your models here.


admin.site.register(products)
admin.site.register(orders)
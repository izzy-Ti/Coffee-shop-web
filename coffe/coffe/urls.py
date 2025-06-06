
from django.contrib import admin
from django.urls import path,include
from .import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name= 'home'),
    path('order/<int:product_id>/', views.order, name = 'order'),
    path('or/', include('products.urls'), name = 'orders')
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

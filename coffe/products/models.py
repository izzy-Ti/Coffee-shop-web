from django.db import models



class products(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    price = models.CharField(max_length=10, default='$')
    description = models.CharField(max_length=255, default='')
    img2 = models.ImageField(default='fallback.png', blank=True)
    def __str__(self):
        return self.name
class orders(models.Model):
    F_name = models.CharField(max_length=50,null=False)
    M_name = models.CharField(max_length=50,null=False)
    phone = models.IntegerField(null=False)
    email = models.CharField(max_length=50, null=False)
    city = models.CharField( max_length=50)
    street = models.CharField( max_length=50)
    def __str__(self):
        return self.email







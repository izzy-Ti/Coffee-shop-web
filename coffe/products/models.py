from django.db import models



class products(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    price = models.IntegerField(max_length=4)
class MyModel(BaseModel):
    description = models.TextField()

    def __str__(self):
        return self.name


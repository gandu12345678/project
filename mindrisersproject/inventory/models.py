from django.db import models
# from django.contrib.auth.models import User
# Create your models here.
from core.models import User

class Category(models.Model):
    name=models.CharField(max_length=20,unique=True)
    class Meta:
        verbose_name_plural='categories'
    def __str__(self):
        return f'{self.name}'
    
    
class Product(models.Model):

    name = models.CharField(max_length=20)

    price = models.DecimalField(max_digits=10, decimal_places=2)
    
    quantity = models.DecimalField(max_digits=10, decimal_places=2)

    description = models.TextField(blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.name} - {self.price} - {self.category}"


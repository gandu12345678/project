from rest_framework import serializers
from . import models

from decimal import Decimal
class CategorySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = models.Category
        fields=(
            "id",
            "name",
        )
        
class ProductSerializer(serializers.ModelSerializer):
    category=serializers.StringRelatedField()
    category_id=serializers.PrimaryKeyRelatedField(
        queryset=models.Category.objects.all(),
        source="category",
    )
    price_with_tax = serializers.SerializerMethodField()
    
    class Meta:
        model = models.Product
        fields=(
           "id", 
           "name",
           "price",
           "price_with_tax",
           'quantity',
           "description",
           "category_id",
           "category",
           
            
        )
    def get_price_with_tax(self,product:models.Product):
        return product.price +(product.price*Decimal(0.13))
        
from django.contrib import admin
from .import models

# Register your models here.
@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display=("id","name",)
    list_per_page=10

@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    list_display=("id","name",'category','price','quantity','description',)
    list_filter=('category',)
    list_editable=('name',)
    list_per_page=10



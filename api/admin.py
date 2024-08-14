from django.contrib import admin
from .models import Stores, StoreItem, Item

# Register your models here.

@admin.register(Stores)
class StoreAdmin(admin.ModelAdmin):
    pass

@admin.register(StoreItem)
class StoreAdmin(admin.ModelAdmin):
    pass

@admin.register(Item)
class StoreAdmin(admin.ModelAdmin):
    pass
from django.db import models

# Create your models here.

class Stores(models.Model):
    name=models.CharField(verbose_name="Магазин", max_length=50, null=False, blank=False, unique=True)

    def __str__(self):
        return self.name


class StoreItem(models.Model):
    item=models.ForeignKey(verbose_name="Товар",to='Item', on_delete=models.CASCADE, related_name='store_items')
    amount=models.IntegerField(verbose_name="Кол-во",null=False, blank=False,default=0)
    store=models.ForeignKey(verbose_name="Магазин",to='Stores', on_delete=models.CASCADE, related_name='items')
    def __str__(self):
        return f'{self.item.name} {self.amount} {self.store.name}'

class Item(models.Model):
    name=models.CharField(verbose_name="Товар",max_length=50, null=False, blank=False)
    description=models.TextField(verbose_name="Описание",null=False, blank=False)
    price=models.IntegerField(verbose_name="Цена за шт",null=False, blank=False, default=0)
    def __str__(self):
        return self.name
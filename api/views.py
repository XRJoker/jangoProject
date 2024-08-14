from django.db.models import Sum
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from .models import Stores,Item,StoreItem
from .forms import StoreForms, AddItemForms, AddItemInStore


# Create your views here.



def store_view(request, store_id, *args, **kwargs):

    if request.method=='POST':
        if request.POST["type"]=="store":
            form=StoreForms(request.POST)
            if form.is_valid():
                store = form.save()
                return HttpResponseRedirect(f"/store/{store.id}")
        else:
            form = AddItemInStore(request.POST)
            if form.is_valid():
                store_item = form.save()
                return HttpResponseRedirect(f"/store/{store_id}")
    store=Stores.objects.get(id=store_id)
    context = {
        'store': store,
        'all_stores': Stores.objects.all(),
        'form': StoreForms(),
        'item_form': AddItemInStore(initial={"store":store}),
    }
    return render(request=request,template_name='store.html', context=context)

def items_view(request, *args, **kwargs):
    if request.method=='POST':
        form=AddItemForms(request.POST)
        if form.is_valid():
            store = form.save()
            return HttpResponseRedirect(f"/items")
    context={
        'all_items': Item.objects.all().annotate(sum=Sum('store_items__amount',default=0)),
        'form': AddItemForms(),
    }
    return render(request=request,template_name='items.html', context=context)

@csrf_exempt
def delete_store_item_view(request, item_id, *args, **kwargs):
    store_item=StoreItem.objects.get(id=item_id)
    store_item.delete()
    return HttpResponse(status=204)

def main_page(request, *args, **kwargs):
    context = {
        'all_stores': Stores.objects.all(),
        "text": "Hello world!",
    }

    return render(request=request,template_name='main.html', context=context)

def item_edit(request, item_id, *args, **kwargs):
    if request.method=='POST':
        form=AddItemForms(request.POST, instance= Item.objects.get(id=item_id))
        if form.is_valid():
            store = form.save()
            return HttpResponseRedirect(f"/items")

    context = {
        'item':AddItemForms(instance= Item.objects.get(id=item_id))
    }
    return render(request=request, template_name='item_edit.html', context=context)

@csrf_exempt
def delete_item_view(request, item_id, *args, **kwargs):
    item=Item.objects.get(id=item_id)
    item.delete()
    return HttpResponse(status=204)
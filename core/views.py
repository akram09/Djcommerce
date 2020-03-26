from django.shortcuts import render
from .models import Item, OrderItem , Order
from django.shortcuts import get_object_or_404, redirect
from django.utils import timezone
from django.contrib import messages
from django.views.generic import ListView, View, DetailView
# Create your views here.


class HomeView(ListView):
    model = Item
    paginate_by = 6
    template_name  = 'home-page.html'

class ItemDetailView(DetailView):
    model = Item
    template_name = "product-page.html"

def add_to_cart(request , slug ):
    item = get_object_or_404(Item , slug = slug)
    orderItem , created = OrderItem.objects.get_or_create(item = item , ordered = False, user = request.user)
    order_qs = Order.objects.filter(user = request.user , ordered =False)
    if order_qs.exists():
        order = order_qs[0]
        if order.items.filter(item__slug = slug).exists() :
            orderItem.quantity += 1
            orderItem.save()
        else:
            order.items.add(orderItem)

    else:
        order = Order.objects.create(user = request.user)
        messages.info(request  , "A new Order have been created")
        order.items.add(orderItem)
    messages.success(request , "Item added successfuly ")
    return redirect("core:item", slug = slug)


def remove_from_cart(request, slug):
    item = get_object_or_404(Item , slug = slug)
    order_qs = Order.objects.filter(user = request.user , ordered =False)
    if order_qs.exists():
        order = order_qs[0]
        if order.items.filter(item__slug = slug ).exists():
            orderItem = OrderItem.objects.get(
            user = request.user ,
            ordered = False,
            item = item
            )
            orderItem.delete()
            messages.success(request , "Product removed from Cart ")
            return redirect("core:item", slug = slug)
        else:
            messages.error( request ,"You havn't purcahsed any product like this ")
            return redirect("core:item", slug = slug)
    else:
        messages.error( request ,"You dont have an active order")
        return redirect("core:item", slug = slug)

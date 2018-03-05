from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse
from .models import OrderItem
from .forms import OrderCreateForm
from cart.cart import Cart

def order_create(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save()
            order.save()
            for item in cart:
                OrderItem.objects.create(order=order,
                                         product=item['product'],
                                         price=item['price'],
                                         quantity=item['quantity'])
            cart.clear()
            return redirect(reverse('payment:charge',kwargs={'order_id':order.id}))
    else:
        form = OrderCreateForm()

    return render(request,
            'orders/order/create.html',
            {'cart': cart, 'form': form})
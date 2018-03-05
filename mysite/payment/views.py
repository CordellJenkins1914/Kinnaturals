from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .forms import SalePaymentForm
from django.template.context_processors import csrf
from cart.cart import Cart
from django.conf import settings
import stripe
from orders.models import Order
from orders.tasks import order_created

# Create your views here.

stripe.api_key = settings.STRIPE_SECRET  

def charge(request,order_id):
    order = get_object_or_404(Order, id=order_id)
    if request.method == "POST":
        form = SalePaymentForm(request.POST)
 
        if form.is_valid(): # charges the card
            try:
                customer = stripe.Charge.create(
                    amount = int(order.get_total_cost() * 100),
                    currency = "USD",
                    card = form.cleaned_data['stripe_id']
                    )
                order.paid = True
                order.save()
                order_created.delay(order.id)
                return render(request,'orders/order/created.html',{'order': order})
            
            except stripe.CardError as ce:
                messages.error(request, "Your card was declined!")
            
    else:
        form = SalePaymentForm()

    args = {'form': form, 'publishable': settings.STRIPE_PUBLISHABLE, 'order':order}
    args.update(csrf(request))

    return render(request,'payment/payment.html',args)
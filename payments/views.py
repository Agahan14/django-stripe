import stripe
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from djangostripe.settings import STRIPE_SECRET_KEY
from .models import (
    Item,
    Order,
    Discount,
    Tax,
)
stripe.api_key = STRIPE_SECRET_KEY


def buy_item(request, item_id):
    item = get_object_or_404(Item, id=item_id)
    session = stripe.checkout.Session.create(
        payment_method_types=['card'],
        line_items=[
            {
                "price_data": {
                    "currency": item.currency,
                    "product_data": {
                        "name": item.name,
                        'description': item.description,
                    },
                "unit_amount": int(item.price * 100),
                },
                "quantity": 1
            }
        ],
        mode='payment',
        success_url=request.build_absolute_uri("/index/"),
        cancel_url=request.build_absolute_uri("/index/"),
    )
    return JsonResponse({'session_id': session.id})


def item_details(request, item_id):
    item = get_object_or_404(Item, id=item_id)
    context = {'item': item}
    return render(request, 'item.html', context)


def buy_order(request, order_id):
    order = get_object_or_404(Order, id=order_id)

    session = stripe.checkout.Session.create(
        payment_method_types=['card'],
        line_items=[
            {
                "price_data": {
                    "currency": "usd",
                    "product_data": {
                        "name": "Order"
                    },
                    "unit_amount": int(order.total_price * 100)
                },
                "quantity": 1
            },


        ],
        mode='payment',
        success_url=request.build_absolute_uri('/index/'),
        cancel_url=request.build_absolute_uri('/index/'),
    )
    return JsonResponse({'session_id': session.id})


def order_details(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    order.calculate_total_price()

    context = {'order': order}
    return render(request, 'order.html', context)


def index(request):
    return render(request, 'index.html')

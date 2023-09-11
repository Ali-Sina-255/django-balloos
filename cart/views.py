from django.shortcuts import render, redirect
from balloon.models import Recent_Product
from .models import Card, CartItem


# Create your views here.
def _cart_id(request):
    cart = request.session.session.key
    if not cart:
        cart = request.session.create()
    return cart


def cart(request):

    return render(request, 'cart/cart.html')


def add_card(request, product_id):
    product = Recent_Product.objects.get(id=product_id)
    try:
        cart = Card.objects.get(cart_id=_cart_id(request))

    except Card.DoesNoExists:
        cart = Card.objects.create(
            card_id=_cart_id(request)
        )
        cart.save()
    try:
        cart_item = CartItem.objects.get(product=product, cart=cart)
        cart_item.quantity += 1
        cart_item.save()
    except CartItem.DoesNoExists:
        cart_item = CartItem.objects.create(
            product=product,
            cart=cart,
            quantity=1

        )
        cart_item.save()
        return redirect('add_cart')

    return render(request, 'cart/add_cart.html')


def remove_card(request):
    pass
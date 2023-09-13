from django.shortcuts import render, redirect, get_object_or_404
from balloon.models import Recent_Product
from .models import Card, CartItem
from django.core.exceptions import ObjectDoesNotExist


# Create your views here.
def _cart_id(request):
    cart = request.session.session_key
    if not cart:
        cart = request.session.create()
    return cart


def cart(request, total=0, quantity=0, cart_items=None):
    try:
        cart = Card.objects.get(card_id=_cart_id(request))
        cart_items = CartItem.objects.filter(cart=cart, is_active=True)
        cart_items_count = cart_items.count()
        for cart_item in cart_items:
            total += (cart_item.product.price * cart_item.quantity)
            quantity += cart_item.quantity
        txt = (2 * total) / 100
        grand_total = total + txt

    except ObjectDoesNotExist:
        pass

    context = {
        'cart_items': cart_items,
        'total': total,
        'quantity': quantity,
        'txt': txt,
        'grand_total': grand_total,
        'cart_items_count': cart_items_count
    }
    return render(request, 'cart/cart.html', context)


def add_card(request, product_id):
    product = Recent_Product.objects.get(id=product_id)
    try:
        cart = Card.objects.get(card_id=_cart_id(request))

    except Card.DoesNotExist:
        cart = Card.objects.create(
            card_id=_cart_id(request)
        )
        cart.save()
    try:
        cart_item = CartItem.objects.get(product=product, cart=cart)
        cart_item.quantity += 1
        cart_item.save()
    except CartItem.DoesNotExist:
        cart_item = CartItem.objects.create(
            product=product,
            cart=cart,
            quantity=1

        )
        cart_item.save()
    return redirect('cart')


def remove_card(request, product_id):
    cart = Card.objects.get(card_id=_cart_id(request))
    product = get_object_or_404(Recent_Product, id=product_id)
    cart_item = CartItem.objects.get(product=product, cart=cart)
    if cart_item.quantity > 1:
        cart_item.quantity -= 1
        cart_item.save()
    else:
        cart_item.delete()
    return redirect('cart')


def remove_cart_item(request, product_id):
    cart = Card.objects.get(card_id=_cart_id(request))
    product = get_object_or_404(Recent_Product, id=product_id)
    cart_item = CartItem.objects.get(cart=cart, product=product)
    cart_item.delete()
    return redirect('cart')

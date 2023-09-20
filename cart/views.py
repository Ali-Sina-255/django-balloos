from django.shortcuts import render, redirect, get_object_or_404
from balloon.models import Recent_Product
from .models import Card, CartItem
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse, JsonResponse


# Create your views here.
def _cart_id(request):
    cart = request.session.session_key
    if not cart:
        cart = request.session.create()
    return cart


def cart(request, total=0, quantity=0, cart_items=None, txt=None, grand_total=None):
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
        'grand_total': grand_total
    }
    return render(request, 'cart/cart.html', context)


def add_card(request, product_id):
    product_id = Recent_Product.objects.get(id=product_id)

    try:
        cart = Card.objects.get(card_id=_cart_id(request))

    except Card.DoesNotExist:
        cart = Card.objects.create(
            card_id=_cart_id(request)
        )
        cart.save()
    try:
        cart_item = CartItem.objects.get(product=product_id, cart=cart)
        cart_item.quantity += 1
        cart_item.save()
    except CartItem.DoesNotExist:
        cart_item = CartItem.objects.create(
            product=product_id,
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



def add_to_cart(request, product_id):
    if request.user.is_authenticated:
        if request.is_ajax():
            # check if the product item is exists
            try:
                product_item = Recent_Product.objects.get(id=product_id)
                # check if the user is has already added product to the cart
                try:
                    check_cart = Card.objects.get(user=request.user, product_item=product_item)
                    check_cart.quantity += 1
                    check_cart.save()
                    return JsonResponse({'status': 'success', 'message': 'add cart was successfully.'})
                except:
                    check_cart = Card.objects.create(
                        user=request.user,
                        quantity=1,
                        product_item=product_item
                    )
                    return JsonResponse({'status': 'success', 'message': 'added product to the cart was successfully.'})
            except:
                return JsonResponse({'status': 'failed', 'message': 'this product is not exists'})

        else:
            return JsonResponse({'status': 'failed', 'message': 'invalid request!'})
    else:
        return JsonResponse({"status": "failed", "message": "Please login to continue"})

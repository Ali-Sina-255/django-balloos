from django.shortcuts import render

# Create your views here.
def add_cart(request):

    return render(request, 'cart/cart.html')
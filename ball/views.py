from django.shortcuts import render, get_object_or_404
from . models import Category, Recent_Products


# Create your views here.
def home(request):
    recent_products = Recent_Products.objects.filter(is_stock=True)
    context = {
        'recent_products': recent_products
    }
    return render(request, 'index.html', context)


def our_blog(request):
    return render(request, 'balloon/our_blog.html')


def product_details(request, pk):
    recents_products = get_object_or_404(Recent_Products, id=pk)
    context = {
        'recent_products': recents_products
    }
    return render(request, 'balloon/product_detail.html', context)


def category(request):
    return {
        'all_category': Category.objects.all()
    }
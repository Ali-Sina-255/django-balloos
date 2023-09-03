from django.shortcuts import render, get_object_or_404, redirect
from .models import Category, Recent_Product, ReviewRating, Blog, Comment
from .forms import CommentForms, ReviewRatingForms
from django.contrib import messages



# Create your views here.
def home(request):
    recent_products = Recent_Product.objects.filter(is_stock=True)
    amount = recent_products.count() 
    context = {
        'recent_products': recent_products,
        'amount': amount
    }
    return render(request, 'index.html', context)


def our_blog(request):
    return render(request, 'balloon/our_blog.html')


def product_details(request, pk):
    recents_products = get_object_or_404(Recent_Product, id=pk)
    reviews = ReviewRating.objects.filter(product_id=recents_products.id, status=True)

    context = {
        'recent_products': recents_products,
        'reviews': reviews

    }
    return render(request, 'balloon/product_detail.html', context)


def category(request):
    return {
        'all_category': Category.objects.all()
    }


def submit_review(request, pk):
    url = request.META.get('HTTP_REFERER')
    if request.method == "POST":
        try:
            review = ReviewRating.objects.get(user__id=request.user.id, product__id=pk)
            forms = ReviewRatingForms(request.POST, instance=review)
            forms.save()
            messages.success(request, 'Thank you! your review has been updated.')
            return redirect(url)
        except ReviewRating.DoesNotExist:
            forms = ReviewRatingForms(request.POST)
            if forms.is_valid():
                data = ReviewRating()
                data.subject = forms.cleaned_data['subject']
                data.review = forms.cleaned_data['review']
                data.rating = forms.cleaned_data['rating']
                data.product_id = pk
                data.user_id = request.user.id
                data.save()
                messages.success(request, 'Thank Your!,your review has been submitted.')
                return redirect(url)


def blog(request):
    blog = Blog.objects.all()
    context = {
        'blogs': blog
    }
    return render(request, 'blog/blog.html', context)


def blog_details(request, pk):  

    blog_details = get_object_or_404(Blog, id=pk)
    context = {
        'blog_details': blog_details
    }
    return render(request, 'blog/blog_details.html', context)


def add_comment(request,pk):
    url = request.META.get('HTTP_REFERER')
    blog = get_object_or_404(Blog, id=pk)
    if request.method == "POST":
        try:
            comment = Comment.objects.get(user__id=request.user.id, blog__id=pk)
            forms = CommentForms(request.POST, instance=comment)
            forms.save()
            messages.success(request, 'Thank you! your comment has been updated.')
            return redirect(url)
        except Comment.DoesNotExist:
            forms = CommentForms(request.POST)
            if forms.is_valid():
                data = Comment()
                data.comment = forms.cleaned_data['comment_name']
                data.comment_body = forms.cleaned_data['comment_body']
                data.blog_id = pk
                data.user_id = request.user.id
                data.save()
                messages.success(request, 'Thank Your!,your comment has been submitted.')
                return redirect(url)

    
    context = {'forms':forms, }
    return render(request, 'blog/blog_details.html',context)


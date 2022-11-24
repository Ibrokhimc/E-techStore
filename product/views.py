from django.shortcuts import render
from .models import Product
# Create your views here.


def product(request, slug):
    product = Product.objects.get(slug=slug)
    return render(request, 'product/product.html', {'product':product})
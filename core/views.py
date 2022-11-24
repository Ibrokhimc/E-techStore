from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import SignUpForm
from product.models import Product, Category, Brand
from django.db.models import Q
# Create your views here.


def frontpage(request):
    products = Product.objects.all()

    return render(request, 'core/frontpage.html', {'products':products})

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)

        if form.is_valid():
            user = form.save()

            login(request, user)
            return redirect('/')
    else:
        form = SignUpForm()
    return render(request, 'core/signup.html', {'form':form})

def loginView(request):
    return render(request, 'core/login.html')

def shop(request):
    products = Product.objects.all()
    category = Category.objects.all()
    brand = Brand.objects.all()

    active_category = request.GET.get('category', ' ')
    if active_category:
        products = products.filter(category__slug = active_category)

    active_brand = request.GET.get('brand', ' ')
    if active_brand:
        products = products.filter(Brand__slug = active_brand)

    query = request.GET.get('query', '')
    if query:
        products =  products.filter(Q(name__icontains = query) | Q(description__icontains = query))

    context = {
        'products':products,
        'category':category,
        'brand':brand,
        'active_category':active_category,
        'active_brand':active_brand

    }
    return render(request, 'core/shop.html', context)




def BlogView(request):
    return render(request, 'nav/blog.html')


def CareerView(request):
    return render(request, 'nav/career.html')


def AboutView(request):
    return render(request, 'nav/about.html')


def ContactView(request):
    return render(request, 'nav/contact.html')
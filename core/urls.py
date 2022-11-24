from django.contrib import admin
from .views import frontpage, shop, signup, BlogView, ContactView, CareerView, AboutView
from django.contrib.auth import views
from django.urls import path
from cart.views import add_to_cart, cart, checkout
from product.views import product
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', frontpage, name='frontpage'),
    path('shop/<slug:slug>/', product, name='product'),
    path('shop/', shop, name='shop'),
    path('add_to_cart/<int:product_id>/', add_to_cart, name='add_to_cart'),
    path('signup/', signup, name='signup'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('login/', views.LoginView.as_view(template_name='core/login.html'), name='login'),
    path('cart/checkout/', checkout, name='checkout'),
    path('cart/', cart, name='cart'),
    path('blog/', BlogView, name='blog'),
    path('about/', AboutView, name='about'),
    path('contact/', ContactView, name='contact'),
    path('career/', CareerView, name='career'),
]



import contact
from django.urls import path, include
from .views import *
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('category/<slug>', CategoryView.as_view(), name='category'),
    path('brand/<slug>', BrandView.as_view(), name='brand'),
    path('product/<slug>', ProductDetail.as_view(), name='product'),
    path('search', SearchView.as_view(), name='search'),
    path('signup', signup, name='signup'),
    path('cart', CartView.as_view(), name='cart'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('add_to_cart/<slug>', add_to_cart, name='add_to_cart'),
    path('reduce_cart/<slug>', reduce_cart, name='reduce_cart'),
    path('delete_cart/<slug>', delete_cart, name='delete_cart'),
    path('product_review/<slug>', product_review, name='product_review'),
    path('product_review/<slug>', product_review, name='product_review'),
    path('wishlist', WishlistView.as_view(), name='wishlist'),
    path('add_to_wishlist/<slug>', add_to_wishlist, name='add_to_wishlist'),
    path('delete_wishlist/<slug>', delete_wishlist, name='delete_wishlist'),
    path('checkout/', Checkout, name='checkout'),
    path('khaltirequest/', KhaltiRequestView.as_view(), name='khaltirequest'),
    path("khaltiverify/", KhaltiVerifyView.as_view(), name="khaltiverify"),
    path("contact", ContactView.as_view(), name="contact"),
    path("contactus", contactus, name="contactus"),
    path("customer_review", CustomerReviewView.as_view(), name="customer_review"),
    path("customer", customerreview, name="customer"),







]

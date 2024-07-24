from django.contrib import admin
from .models import *

class OrderItemTubleinline(admin.TabularInline):
    model = OrderItem

class OrderAdmin(admin.ModelAdmin):
    inlines = [OrderItemTubleinline]

class AdminProduct(admin.ModelAdmin):
    list_display = ['name','price','category','brand','labels','stock']

class AdminCart(admin.ModelAdmin):
    list_display = ['username','items','quantity','total','date']

class AdminOrderDetail(admin.ModelAdmin):
    list_display = ['username','firstname','lastname','email','phone_number','address','payment_method','total','payment_completed','order_status']

class AdminContact(admin.ModelAdmin):
    list_display = ['name','email','subject','message']

class AdminCustomerReview(admin.ModelAdmin):
    list_display = ['name', 'post', 'image', 'comment']

admin.site.register(Category)
admin.site.register(Slider)
admin.site.register(Ad)
admin.site.register(Brand)
admin.site.register(Product,AdminProduct)
admin.site.register(CustomerReview,AdminCustomerReview)
admin.site.register(Cart,AdminCart)
admin.site.register(ProductReview)
admin.site.register(Wishlist)
admin.site.register(OrderDetail,AdminOrderDetail)
admin.site.register(OrderItem)
admin.site.register(Contact,AdminContact)

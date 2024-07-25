from django.contrib import admin
from .models import *

class OrderItemTubleinline(admin.TabularInline):
    model = OrderItem

class AdminProduct(admin.ModelAdmin):
    list_display = ['name','price','category','brand','labels','stock']

class AdminCart(admin.ModelAdmin):
    list_display = ['username','items','quantity','total','date']

class AdminOrderDetail(admin.ModelAdmin):
    inlines = [OrderItemTubleinline]
    list_display = ['username','firstname','lastname','email','phone_number','address','payment_method','total','payment_completed','order_status']
    search_fields = ['username','firstname','email','phone_number']

class AdminContact(admin.ModelAdmin):
    list_display = ['name','email','subject','message']

class AdminCustomerReview(admin.ModelAdmin):
    list_display = ['name', 'post', 'image', 'comment']

class AdminOrderItem(admin.ModelAdmin):
    list_display = ['order', 'product', 'quantity', 'price']

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
admin.site.register(OrderItem,AdminOrderItem)
admin.site.register(Contact,AdminContact)

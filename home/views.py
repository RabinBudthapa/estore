from django.http import JsonResponse
import requests

# Create your views here.
from .forms import CheckoutForm
from .models import *
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.
from django.views import View

class Base(View):
    views={}
class HomeView(Base):
    def get(self,request):
        self.views['categories']=Category.objects.all()
        self.views['brands'] = Brand.objects.all()
        self.views['sliders'] = Slider.objects.all()
        self.views['hots'] = Product.objects.filter(labels='hot')
        self.views['news'] = Product.objects.filter(labels='new')
        self.views['reviews'] = CustomerReview.objects.all()
        self.views['ads']=Ad.objects.all()
        self.views['count_cart'] = Cart.objects.filter(username = request.user.username,checkout = False).count
        self.views['count_wishlist'] = Wishlist.objects.filter(username=request.user.username, checkout=False).count
        return render(request,'index.html',self.views)

class CategoryView(Base):
    def get(self,request,slug):
        cat_id = Category.objects.get(slug = slug).id
        self.views['cat_products'] = Product.objects.filter(category_id = cat_id)
        self.views['categories'] = Category.objects.all()
        self.views['brands'] = Brand.objects.all()
        self.views['sales'] = Product.objects.filter(labels='sale')
        self.views['count_cart'] = Cart.objects.filter(username=request.user.username, checkout=False).count
        self.views['count_wishlist'] = Wishlist.objects.filter(username=request.user.username, checkout=False).count
        return render(request,'category.html',self.views)

class BrandView(Base):
    def get(self,request,slug):
        brand_id = Brand.objects.get(slug = slug).id
        self.views['brand_products'] = Product.objects.filter(brand_id = brand_id)
        self.views['categories'] = Category.objects.all()
        self.views['brands'] = Brand.objects.all()
        self.views['sales'] = Product.objects.filter(labels='sale')
        return render(request,'brand.html',self.views)


class ProductDetail(Base):
    def get(self,request,slug):
        self.views['product_detail'] = Product.objects.filter(slug=slug)
        self.views['sales'] = Product.objects.filter(labels='sale')
        product_category = Product.objects.get(slug=slug).category_id
        self.views['related_products'] = Product.objects.filter(category_id = product_category)
        product_brand = Product.objects.get(slug=slug).brand_id
        self.views['brand_related_product'] = Product.objects.filter(brand_id = product_brand)
        self.views['count_cart'] = Cart.objects.filter(username=request.user.username, checkout=False).count()
        self.views['count_wishlist'] = Wishlist.objects.filter(username=request.user.username, checkout=False).count
        self.views['product_reviews'] = ProductReview.objects.filter(slug=slug)
        self.views['categories'] = Category.objects.all()
        return render(request,'product-detail.html',self.views)

def product_review(request,slug):
    if Product.objects.filter(slug = slug):
        if request.method == 'POST':
            username = request.user.username
            star = request.POST['star']
            comment = request.POST['comment']
            ProductReview.objects.create(
                username = username,
                slug = slug,
                star = star,
                comment = comment
            ).save()
    else:
        return redirect(f'/product/{slug}')
    return redirect(f'/product/{slug}')



class SearchView(Base):
    def get(self,request):
        if request.method == 'GET':
            query = request.GET['query']
            if query != "":
              self.views['search_products'] = Product.objects.filter(name__icontains = query)
            else:
               redirect('/')
        self.views['categories'] = Category.objects.all()
        self.views['brands'] = Brand.objects.all()
        self.views['sales'] = Product.objects.filter(labels='sale')
        self.views['count_cart'] = Cart.objects.filter(username=request.user.username, checkout=False).count
        self.views['count_wishlist'] = Wishlist.objects.filter(username=request.user.username, checkout=False).count
        return render(request,'search.html',self.views)


def signup(request):
    if request.method == "POST":
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        password = request.POST['password']
        cpassword = request.POST['cpassword']
        if password == cpassword:
            if User.objects.filter(username = username).exists():
                messages.error(request,"the username is already used")
                return redirect('/signup')
            elif User.objects.filter(email = email).exists():
                messages.error(request,"this email is already exist")
                return redirect('/signup')
            else:
                data = User.objects.create_user(
                    first_name = fname,
                    last_name = lname,
                    email = email,
                    username = username,
                    password = password,
                )
                data.save()
        else:
            messages.error(request,"password doesn't match")
            return redirect('/signup')
    return render(request,'signup.html')



class WishlistView(Base):
    def get(self, request):
        username = request.user.username
        self.views['count_wishlist'] = Wishlist.objects.filter(username=request.user.username, checkout=False).count
        self.views['my_wishlist'] = Wishlist.objects.filter(username=username)
        return render(request, 'wishlist.html', self.views)

def add_to_wishlist(request,slug):
        username = request.user.username
        if Wishlist.objects.filter(username=username, slug=slug, checkout=False):
            return redirect('/wishlist')

        else:
          data = Wishlist.objects.create(
            username=username,
            slug=slug,
            items=Product.objects.filter(slug=slug)[0]
          )
          data.save()
          return redirect('/wishlist')

def delete_wishlist(request,slug):
    username = request.user.username
    if Wishlist.objects.filter(slug = slug,username = username,checkout = False):
        Wishlist.objects.filter(slug = slug, username = username, checkout = False).delete()
    return redirect('/wishlist')




class CartView(Base):
    def get(self,request):
        username = request.user.username
        self.views['count_cart'] = Cart.objects.filter(username=request.user.username, checkout=False).count
        self.views['count_wishlist'] = Wishlist.objects.filter(username=request.user.username, checkout=False).count
        self.views['my_cart'] = Cart.objects.filter(username = username)
        my_cart = Cart.objects.filter(username=username,checkout=False)
        s = 0
        for i in my_cart:
            s = s + i.total
        self.views['all_total'] = s
        delivery_charge = 50
        self.views['grand_total'] = s + delivery_charge
        return render(request,'cart.html',self.views)


def add_to_cart(request,slug):
    username = request.user.username
    if Cart.objects.filter(username = username,slug = slug,checkout = False):
        price = Product.objects.get(slug = slug).price
        discounted_price = Product.objects.get(slug=slug).discounted_price
        quantity = Cart.objects.get(slug = slug).quantity
        quantity = quantity + 1
        if discounted_price > 0:
            total = discounted_price * quantity
        else:
            total = price * quantity

        Cart.objects.filter(username=username, slug=slug, checkout=False).update(
            quantity = quantity,
            total = total,
        )
        return redirect('/cart')



    else:
        price = Product.objects.get(slug=slug).price
        discounted_price = Product.objects.get(slug=slug).discounted_price
        quantity = 1
        if discounted_price > 0:
            total = discounted_price
        else:
            total = price
        data = Cart.objects.create(
            username = username,
            slug = slug,
            quantity = quantity,
            total = total,
            items = Product.objects.filter(slug = slug)[0],
            grandtotal = 0

        )
        data.save()
        return redirect('/cart')


def delete_cart(request,slug):
    username = request.user.username
    if Cart.objects.filter(slug = slug,username = username,checkout = False):
        Cart.objects.filter(slug = slug, username = username, checkout = False).delete()
    return redirect('/cart')
def reduce_cart(request,slug):
    username = request.user.username
    if Cart.objects.filter(username=username, slug=slug, checkout=False):
        price = Product.objects.get(slug=slug).price
        discounted_price = Product.objects.get(slug=slug).discounted_price
        quantity = Cart.objects.get(slug=slug).quantity
        if quantity > 1:
          quantity = quantity - 1
          if discounted_price > 0:
            total = discounted_price * quantity
          else:
              total = price * quantity

          Cart.objects.filter(username=username, slug=slug, checkout=False).update(
              quantity=quantity,
              total=total,
          )
          return redirect('/cart')
        else:
            return redirect('/cart')


def login_user (request):
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(request, username=username, password=password)
		if user is not None:
			login(request, user)
			messages.success(request,('Youre logged in'))
			return redirect('/')
		else:
			messages.success(request,('Error logging in'))
			return redirect('login')
	else:
		return render(request, 'registration/login.html', {})

def logout_user(request):
	logout(request)
	messages.success(request,('Youre now logged out'))
	return redirect('/')



def Checkout(request):
    if request.method == 'POST':
        form =CheckoutForm(request.POST, user=request.user)
        if form.is_valid():
            order_detail = form.save(commit=False)
            order_detail.username = request.user.username
            order_detail.save()

            # Calculate subtotal and grand total
            username = request.user.username
            cart_items = Cart.objects.filter(username=username, checkout=False)
            subtotal = sum(i.total for i in cart_items)
            delivery_charge = 50
            grand_total = subtotal + delivery_charge
            cart_items.update(grandtotal=grand_total)

            # Update order_detail with grand total
            order_detail.total = grand_total
            order_detail.save()

            # Create OrderItem for each item in the cart
            for item in cart_items:
                OrderItem.objects.create(
                    order=order_detail,
                    product=item.items,
                    quantity=item.quantity,
                    price=item.total,
                )

            if order_detail.payment_method == "Khalti":
              return redirect("/khaltirequest" + "?o_id=" + str(order_detail.id))
            else:
                return redirect('/')
    else:
        form = CheckoutForm(user=request.user)

    return render(request, 'checkout.html', {'form': form})



class KhaltiRequestView(Base):
    def get(self, request, *args, **kwargs):
        username = request.user.username
        self.views['my_cart'] = Cart.objects.filter(username=username)
        o_id = request.GET.get("o_id")
        order = OrderDetail.objects.get(id=o_id)
        context = {
            "order" : order,
            **self.views
        }
        return render(request, "khaltirequest.html", context)

class KhaltiVerifyView(View):
    def get(self, request, *args, **kwargs):
        token = request.GET.get("token")
        amount = request.GET.get("amount")
        o_id = request.GET.get("order_id")
        print(token, amount, o_id)
        url = "https://khalti.com/api/v2/payment/verify/"

        payload = {
            'token': token,
            'amount': amount
        }

        headers = {
            'Authorization': 'Key test_secret_key_679f35b61ae54acabd42b259a3c4084e'
        }

        response = requests.request("POST", url, headers=headers, json=payload)
        order_obj = OrderDetail.objects.get(id=o_id)
        resp_dict = response.json()
        print(resp_dict)
        if resp_dict.get("idx"):
            success = True
        else:
            success = False

        data = {
            "success" : success
        }
        return JsonResponse(data)


class ContactView(Base):
    def get(self,request):
        return render(request,'contact.html',self.views)

def contactus(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']
        Contact.objects.create(
            name=name,
            email=email,
            subject=subject,
            message=message
        ).save()

    return redirect('/')

class CustomerReviewView(Base):
    def get(self,request):
        return render(request,'customer-review.html',self.views)


def customerreview(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        post = request.POST.get('post')
        image = request.FILES.get('image')
        comment = request.POST.get('comment')
        CustomerReview.objects.create(
            name=name,
            post=post,
            image=image,
            comment=comment
        ).save()

    return redirect('/')





















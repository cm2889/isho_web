from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def products(request):
    return render(request, 'product/products.html')


def product_detail(request, product_slug):
    return render(request, 'product/product_detail.html')


def cart(request):
    return render(request, 'cart/cart.html')


def checkout(request):
    return render(request, 'cart/checkout.html')


def wishlist(request):
    return render(request, 'cart/wishlist.html')

def profile(request):
    return render(request, 'order/profile.html')

def order_tracking(request):
    return render(request, 'order/order_tracking.html')

def signup_business(request):
    return render(request, 'business/signup_business.html')

def isho_business(request):
    return render(request, 'business/isho_business.html')

def profile_detail(request):
    return render(request, 'order/profile_detail.html')

def product_list(request):
    return render(request, 'product/product_list.html')

def about(request):
    return render(request, 'footer_pages/about.html')

def sustainability(request):
    return render(request, 'footer_pages/sustainability.html')

def news(request):
    return render(request, 'footer_pages/news.html')

def campaigns(request):
    return render(request, 'footer_pages/campaings.html')

def store_location(request):
    return render(request, 'footer_pages/store_location.html')

def services(request):
    return render(request, 'footer_pages/services.html')

def faqs(request):
    return render(request, 'footer_pages/faqs.html')

def contact(request):
    return render(request, 'footer_pages/contack.html')

def bring_light_to_lives(request):
    return render(request, 'footer_pages/bringlighttolives.html')

def events(request):
    return render(request, 'footer_pages/events.html')

def innovation(request):
    return render(request, 'footer_pages/innovation.html')

def ideas(request):
    return render(request, 'footer_pages/ideas.html')

def dramabox(request):
    return render(request, 'footer_pages/dramabox.html')

def ewmp(request):
    return render(request, 'footer_pages/ewmp.html')

def vieworder_details(request):
    return render(request, 'order/vieworder_details.html')


def login(request):
    return render(request, 'signup/login.html')


def register(request):
    return render(request, 'signup/registation.html')

def product_detail_page(request):
    return render(request, 'product/product_view.html')

def shipping_delivery(request):
    return render(request, 'footer_pages/shipping_delivery.html')

def privacy_policy(request):
    return render(request, 'footer_pages/privacy_policy.html')

def cancellation_returnd(request):
    return render(request, 'footer_pages/cancellation_returnd.html')
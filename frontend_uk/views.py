from django.shortcuts import render


def index(request):
    return render(request, 'uk/index.html')


def products(request):
    return render(request, 'uk/product/products.html')


def product_detail(request, product_slug):
    return render(request, 'uk/product/product_detail.html')


def cart(request):
    return render(request, 'uk/cart/cart.html')

def checkout(request):
    return render(request, 'uk/cart/checkout.html')

def wishlist(request):
    return render(request, 'uk/cart/wishlist.html')

def profile(request):
    return render(request, 'uk/order/profile.html')

def order_tracking(request):
    return render(request, 'uk/order/order_tracking.html')

def signup_business(request):
    return render(request, 'uk/business/signup_business.html')

def isho_business(request):
    return render(request, 'uk/business/isho_business.html')

def profile_detail(request):
    return render(request, 'uk/order/profile_detail.html')

def product_list(request):
    return render(request, 'uk/product/product_list.html')

def about(request):
    return render(request, 'uk/footer_pages/about.html')

def sustainability(request):
    return render(request, 'uk/footer_pages/sustainability.html')

def news(request):
    return render(request, 'uk/footer_pages/news.html')

def campaigns(request):
    return render(request, 'uk/footer_pages/campaings.html')

def store_location(request):
    return render(request, 'uk/footer_pages/store_location.html')

def services(request):
    return render(request, 'uk/footer_pages/services.html')

def faqs(request):
    return render(request, 'uk/footer_pages/faqs.html')

def contact(request):
    return render(request, 'uk/footer_pages/contack.html')

def bring_light_to_lives(request):
    return render(request, 'uk/footer_pages/bringlighttolives.html')

def events(request):
    return render(request, 'uk/footer_pages/events.html')

def innovation(request):
    return render(request, 'uk/footer_pages/innovation.html')

def ideas(request):
    return render(request, 'uk/footer_pages/ideas.html')

def dramabox(request):
    return render(request, 'uk/footer_pages/dramabox.html')

def ewmp(request):
    return render(request, 'uk/footer_pages/ewmp.html')

def vieworder_details(request):
    return render(request, 'uk/order/vieworder_details.html')


def login(request):
    return render(request, 'uk/signup/login.html')


def register(request):
    return render(request, 'uk/signup/registation.html')

def product_detail_page(request):
    return render(request, 'uk/product/product_view.html')
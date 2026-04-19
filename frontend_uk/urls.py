from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('products/', views.products, name='products'),
    path('product-detail/', views.product_detail_page, name='product_detail_page'),
    path('product/<str:product_slug>/', views.product_detail, name='product_detail'),
    path('cart/', views.cart, name='cart'),
    path('wishlist/', views.wishlist, name='wishlist'),
    path('checkout/', views.checkout, name='checkout'),
    path('profile/', views.profile, name='profile'),
    path('order-tracking/', views.order_tracking, name='order_tracking'),
    path('signup-business/', views.signup_business, name='signup_business'),
    path('isho-business/', views.isho_business, name='isho_business'),
    path('profile-detail/', views.profile_detail, name='profile_detail'),
    path('product-list/', views.product_list, name='product_list'),
    path('about/', views.about, name='about'),
    path('sustainability/', views.sustainability, name='sustainability'),
    path('news/', views.news, name='news'),
    path('campaigns/', views.campaigns, name='campaigns'),
    path('store-location/', views.store_location, name='store_location'),
    path('services/', views.services, name='services'),
    path('faqs/', views.faqs, name='faqs'),
    path('contact/', views.contact, name='contact'),
    path('bringlighttolives/', views.bring_light_to_lives, name='bringlighttolives'),
    path('events/', views.events, name='events'),
    path('innovation/', views.innovation, name='innovation'),
    path('ideas/', views.ideas, name='ideas'),
    path('dramabox/', views.dramabox, name='dramabox'),
    path('ewmp/', views.ewmp, name='ewmp'),
    path('vieworder-details/', views.vieworder_details, name='vieworder-details'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    

    
    
]
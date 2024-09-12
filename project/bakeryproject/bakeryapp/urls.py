from django.urls import path
from .views import homepage, products, contact

urlpatterns = [
    path('', homepage, name='homepage'),
    path('products/', products, name='products'),
    path('contact/', contact, name='contact'),
]

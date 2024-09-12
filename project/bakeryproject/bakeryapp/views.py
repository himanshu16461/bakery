# from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from .models import Product, ContactMessage
from .forms import ContactForm

def homepage(request):
    return render(request, 'core/homepage.html')

def products(request):
    items = Product.objects.all()
    return render(request, 'core/products.html', {'items': items})

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('homepage')
    else:
        form = ContactForm()
    return render(request, 'core/contact.html', {'form': form})

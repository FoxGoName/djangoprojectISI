from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView
from store.models import Product

# Create your views here.
def frontPage(request):

    products = Product.objects.all()
    context = {
        'products': products
    }
    return render(request, 'front.html', context)

def contact(request):
    return render(request, 'contact.html')

def productManagePage(request):

    products = Product.objects.all()
    context = {
        'products': products
    }
    return render(request, 'product.html', context)


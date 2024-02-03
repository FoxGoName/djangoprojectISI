from django.shortcuts import render, get_object_or_404
from django.views.generic import CreateView, UpdateView
from .models import Product

# Create your views here.
def productDetail(request, slug):
    product = get_object_or_404(Product, slug=slug)

    context = {
        'product': product
    }

    return render(request, 'productDetail.html', context)
class productCreateView(CreateView):
    model = Product
    template_name = "addProduct.html"
    fields = '__all__'

class editProductView(UpdateView):
    model = Product
    template_name = "editProduct.html"
    fields = '__all__'
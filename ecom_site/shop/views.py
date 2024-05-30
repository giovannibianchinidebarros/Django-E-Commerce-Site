from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Product

# Create your views here.


def index(request):
    product_objects = Product.objects.all()
    item_name = request.GET.get('item_name')

    # Search item
    if item_name:
        product_objects = product_objects.filter(title__icontains=item_name)

    # Paginator
    paginator = Paginator(product_objects, per_page=8)
    page = request.GET.get('page')
    product_objects = paginator.get_page(page)

    return render(request, 'shop/index.html', {'product_objects': product_objects})


def detail(request, id):
    product_object = Product.objects.get(id=id)

    return render(request, 'shop/detail.html', {'product_object': product_object})


def checkout(request):
    key = request.COOKIES.get('key')
    return render(request, 'shop/checkout.html', {"key": key})

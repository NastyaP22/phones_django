from django.shortcuts import render, redirect, get_object_or_404
from .models import Phone


def index(request):
    return redirect('catalog')


def show_catalog(request):
    template = 'catalog.html'
    request_content = request.GET.get('sort')
    if request_content == 'name':
        phones = Phone.objects.order_by('name')
    elif request_content == 'min_price':
        phones = Phone.objects.order_by('price')
    elif request_content == 'max_price':
        phones = Phone.objects.order_by('-price')
    else:
        phones = Phone.objects.all()
    context = {'phones': phones}
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    phone = get_object_or_404(Phone, slug=slug)
    context = {'phone': phone}
    return render(request, template, context)

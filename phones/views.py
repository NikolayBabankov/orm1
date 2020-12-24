from django.shortcuts import render
from phones.models import Phone
from django.urls import reverse


def show_catalog(request):
    template = 'catalog.html'
    phone_query = Phone.objects.all()
    phones_filter = request.GET.get('sort')
    if phones_filter == 'min':
        phone_query = Phone.objects.order_by('price')
    if phones_filter == 'name':
        phone_query = Phone.objects.order_by('name')
    if phones_filter == 'max':
        phone_query = Phone.objects.order_by('-price')
    max_price = reverse('catalog') + f'?sort=max'
    mix_price = reverse('catalog') + f'?sort=min'
    name_phone = reverse('catalog') + f'?sort=name'
    context = {'phone': phone_query,
    'max':max_price,
    'min': mix_price,
    'name':name_phone}
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    phone = Phone.objects.filter(slug=slug)
    context = {'name':phone}
    return render(request, template, context)

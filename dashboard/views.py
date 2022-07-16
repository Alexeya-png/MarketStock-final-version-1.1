from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Product, Order
from .forms import ProductForm, OrderForm
from django.contrib.auth.models import User


@login_required(login_url='Вход')
def index(request):
    orders = Order.objects.all()
    products = Product.objects.all()
    items_count = products.count()
    orders_count = orders.count()
    markets_count = User.objects.all().count()
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.market = request.user.profile
            instance.save()
            return redirect('Главная страница')
    else:
        form = OrderForm()
    context={
        'orders': orders,
        'form': form,
        'products': products,
        'items_count': items_count,
        'markets_count': markets_count,
        'orders_count': orders_count,

    }
    return render(request, 'dashboard/index.html',context)


@login_required(login_url='Вход')
def market(request):
    markets = User.objects.all()
    markets_count = markets.count()
    orders_count = Order.objects.all().count()
    items_count = Product.objects.all().count()
    context={
        'markets': markets,
        'markets_count': markets_count,
        'orders_count': orders_count,
        'items_count': items_count,
    }
    return render(request, 'dashboard/market.html', context)

@login_required(login_url='Вход')
def market_detail(request, pk):
    markets = User.objects.get(id=pk)
    context = {
        'markets': markets,
    }

    return render(request, 'dashboard/market_detail.html', context)


@login_required(login_url='Вход')
def product(request):
    items = Product.objects.all()
    items_count = items.count()
    markets_count = User.objects.all().count()
    orders_count = Order.objects.all().count()



    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Продукты')
    else:
        form = ProductForm()
    context={
        'items': items,
        'form': form,
        'markets_count': markets_count,
        'orders_count': orders_count,
        'items_count': items_count,
    }
    return render(request, 'dashboard/product.html', context)


@login_required(login_url='Вход')
def order(request):
    orders = Order.objects.all()
    orders_count = orders.count
    markets_count = User.objects.all().count()
    items_count = Product.objects.all().count()


    context={
        'orders':orders,
        'markets_count': markets_count,
        'orders_count': orders_count,
        'items_count': items_count
    }
    return render(request, 'dashboard/order.html', context)


@login_required(login_url='Вход')
def product_delete(request, pk):
    item = Product.objects.get(id=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('Продукты')
    context = {
        'item': item
    }
    return render(request, 'dashboard/product_delete.html', context)


@login_required(login_url='Вход')
def product_edit(request, pk):
    item = Product.objects.get(id=pk)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('Продукты')
    else:
        form = ProductForm(instance=item)
    context = {
        'form': form,
    }
    return render(request, 'dashboard/product_edit.html', context)


@login_required(login_url='Вход')
def order_delete(request, pk):
    order = Order.objects.get(id=pk)
    if request.method == 'POST':
        order.delete()
        return redirect('Продукты')
    context = {
        'orders': order
    }
    return render(request, 'dashboard/order_delete.html', context)


@login_required(login_url='Вход')
def market_delete(request, pk):
    markets = User.objects.get(id=pk)
    if request.method == 'POST':
        markets.delete()
        return redirect('Супермаркеты')
    context = {
        'markets': markets
    }
    return render(request, 'dashboard/market_delete.html', context)

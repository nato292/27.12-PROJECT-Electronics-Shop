from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

from .models import Product, UserProfile, Order
from .forms import ShippingAddressForm


# =========================
# Головна / список товарів
# =========================
def product_list(request):
    products = Product.objects.filter(available=True)
    return render(request, 'electricapp/product_list.html', {
        'products': products
    })


# =========================
# Деталі товару
# =========================
def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk, available=True)
    return render(request, 'electricapp/product_detail.html', {
        'product': product
    })


# =========================
# Вхід
# =========================
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('product_list')
        else:
            return render(request, 'electricapp/login.html', {
                'error': 'Невірний логін або пароль'
            })

    return render(request, 'electricapp/login.html')


# =========================
# Реєстрація
# =========================
def register_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')

        if password != password2:
            return render(request, 'electricapp/register.html', {
                'error': 'Паролі не співпадають'
            })

        if User.objects.filter(username=username).exists():
            return render(request, 'electricapp/register.html', {
                'error': 'Користувач уже існує'
            })

        user = User.objects.create_user(
            username=username,
            email=email,
            password=password
        )

        UserProfile.objects.get_or_create(user=user)
        login(request, user)

        return redirect('product_list')

    return render(request, 'electricapp/register.html')


# =========================
# Вихід
# =========================
@login_required
def logout_view(request):
    logout(request)
    return redirect('product_list')


# =========================
# Профіль
# =========================
@login_required
def profile(request):
    UserProfile.objects.get_or_create(user=request.user)
    return render(request, 'electricapp/profile.html')


# =========================
# Мої замовлення
# =========================
@login_required
def my_orders(request):
    orders = Order.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'electricapp/my_orders.html', {
        'orders': orders
    })


# =========================
# Деталі замовлення
# =========================
@login_required
def order_detail(request, order_id):
    order = get_object_or_404(
        Order,
        id=order_id,
        user=request.user
    )

    items = order.items.all()
    for item in items:
        item.total_price = item.quantity * item.price

    return render(request, 'electricapp/order_detail.html', {
        'order': order,
        'items': items,
        'shipping': getattr(order, 'shipping_address', None),
    })



#http://127.0.0.1:8000/
#http://127.0.0.1:8000/product/1/
#http://127.0.0.1:8000/product/2/
#http://127.0.0.1:8000/product/3/
#http://127.0.0.1:8000/admin/
#http://127.0.0.1:8000/profile/ Релог + Другой акк зайти
#http://127.0.0.1:8000/my-orders/
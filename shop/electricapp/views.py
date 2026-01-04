from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Product, UserProfile
from .forms import ShippingAddressForm


def product_list(request):
    products = Product.objects.filter(available=True)
    return render(request, 'electricapp/product_list.html', {
        'products': products
    })


def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk, available=True)
    return render(request, 'electricapp/product_detail.html', {
        'product': product
    })


@login_required
def profile(request):
    UserProfile.objects.get_or_create(user=request.user)

    return render(request, 'electricapp/profile.html')



#http://127.0.0.1:8000/
#http://127.0.0.1:8000/product/1/
#http://127.0.0.1:8000/product/2/
#http://127.0.0.1:8000/product/3/
#http://127.0.0.1:8000/admin/
#http://127.0.0.1:8000/profile/ Релог + Другой акк зайти
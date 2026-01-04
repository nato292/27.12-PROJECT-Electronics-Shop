from django.urls import path
from .views import product_list, product_detail, profile, my_orders, order_detail
from . import views

urlpatterns = [
    # products
    path('', product_list, name='product_list'),
    path('product/<int:pk>/', product_detail, name='product_detail'),

    # profile
    path('profile/', profile, name='profile'),

    # orders
    path('my-orders/', my_orders, name='my_orders'),
    path('my-orders/<int:order_id>/', order_detail, name='order_detail'),

    #login, register, logout
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('logout/', views.logout_view, name='logout'),
]

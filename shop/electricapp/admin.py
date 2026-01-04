from django.contrib import admin
from .models import Category, Product, UserProfile, Order, OrderItem, ShippingAddress

class ProductInline(admin.TabularInline):
    model = Product
    extra = 0

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}
    inlines = [ProductInline]

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price', 'available')
    list_filter = ('available', 'category')
    list_editable = ('available',)
    search_fields = ('name',)

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'phone', 'city')
    search_fields = ('user__username', 'phone', 'city')

class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 0


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'user',
        'status',
        'is_paid',
        'total_price',
        'created_at',
    )
    list_filter = ('status', 'is_paid', 'created_at')
    search_fields = ('user__username', 'id')
    readonly_fields = ('created_at',)
    inlines = [OrderItemInline]
    date_hierarchy = 'created_at'

@admin.register(ShippingAddress)
class ShippingAddressAdmin(admin.ModelAdmin):
    list_display = ('order', 'city', 'address', 'postal_code')
    search_fields = ('city', 'address', 'postal_code')

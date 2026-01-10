from .models import Product


class SessionCart:
    SESSION_KEY = 'cart'

    def __init__(self, request):
        self.session = request.session
        cart = self.session.get(self.SESSION_KEY)

        if not cart:
            cart = self.session[self.SESSION_KEY] = {}

        self.cart = cart

    def add(self, product_id, quantity=1):
        product_id = str(product_id)

        if product_id not in self.cart:
            self.cart[product_id] = 0

        self.cart[product_id] += quantity
        self.save()

    def remove(self, product_id):
        product_id = str(product_id)

        if product_id in self.cart:
            del self.cart[product_id]
            self.save()

    def clear(self):
        self.session[self.SESSION_KEY] = {}
        self.save()

    def save(self):
        self.session.modified = True

    def get_products(self):
        product_ids = self.cart.keys()
        products = Product.objects.filter(id__in=product_ids)

        items = []
        for product in products:
            items.append({
                'product': product,
                'quantity': self.cart[str(product.id)],
                'total_price': product.price * self.cart[str(product.id)],
            })
        return items

    def get_total_price(self):
        return sum(item['total_price'] for item in self.get_products())

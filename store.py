class Store:
    """Represents a store, that sells many products."""

    def __init__(self, products):
        """Args:
            products (list): List of products.
        """
        self.products = products

    def add_product(self, product):
        """Adds a new product to store."""
        self.products.append(product)

    def remove_product(self, product):
        """Removes a product from store."""
        self.products.remove(product)

    def get_total_quantity(self):
        """calculates total amount of product in store."""
        total = 0
        for product in self.products:
            total += product.get_quantity()
        return total

    def get_all_products(self):
        """Returns all active products."""
        active_products = []
        for product in self.products:
            if product.is_active():
                active_products.append(product)
        return active_products

    def order(self, shopping_list):
        """orders the shopping list
        Args:
             shopping list (list): Lists of tupples (product, quantity)"""
        total_price = 0
        for product, quantity in shopping_list:
            price = product.buy(quantity)
            total_price += price
        return total_price


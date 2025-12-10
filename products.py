class Product:
    """ Represents a product type in store."""

    def __init__(self, name, price, quantity):
        """
        :param name: Name of the product
        :param price: Price of the product
        :param quantity: Quantity of product
        Raises:
            ValueError: If name is empty or price/quantity negativ.
        """
        if not name or name.strip() == "":
            raise ValueError("Name must not be empty")
        if price < 0:
            raise ValueError("Price must not be negativ")
        if quantity < 0:
            raise ValueError("Quantity must not be negativ")

        self.name = name
        self.price = price
        self.quantity = quantity
        self.active = True

    def get_quantity(self):
        """Get Methode for quantity
        Returns:
            Actual quantity of product
        """
        return self.quantity

    def set_quantity(self, quantity):
        """Setter-Method for the quantity.
        Deactivates the product if quantity is 0.
        Args:
            quantity(int): New quantity
        """
        self.quantity = quantity
        if self.quantity == 0:
            self.deactivate()

    def is_active(self):
        """Get method for active.
        Returns:
            bool: True if product is active, else False.
        """
        return self.active

    def activate(self):
        """Activates the product."""
        self.active = True

    def deactivate(self):
        """Deactivates the product."""
        self.active = False

    def show(self):
        """Returns a string representation of the product."""
        print(f"{self.name}, Price:{self.price}, Quantity:{self.quantity}")

    def buy(self, quantity):
        """Buys a product.
        Args: quantity(int): quantity to buy
        Returns: float: Total Sum of buy.
        Raises:
            ValueError: If quantity is not correct
            Exception: If product is deactivated.
        """
        if quantity <= 0:
            raise ValueError("Quantity must be positiv")
        if not self.is_active():
            raise Exception("Product is not activ")
        if quantity > self.quantity:
            raise Exception("Not enough in store")

        total_price = self.price * quantity
        self.set_quantity(self.quantity - quantity)
        return total_price


# CLASSES AND METHODS
class Store(object):
    def __init__(self, name):
        """
        Initializes a new store with a name.
        """
        # your code goes here!
        self.name = name
        self.products = []

    def add_product(self, product):
        """
        Adds a product to the list of products in this store.
        """
        # your code goes here!
        self.products.append(product)

    def print_products(self):
        """
        Prints all the products of this store in a nice readable format.
        """
        # your code goes here!
        print("-------------------------------")
        print("%s:" % self.name)
        for product in self.products:
            print(product)
            print()


class Product(object):
    def __init__(self, name, description, price):
        """
        Initializes a new product with a name, a description, and a price.
        """
        # your code goes here!
        self.name = name
        self.description = description
        self.price = price


    def __str__(self):
        # your code goes here!
        return "\tProduct name: %s\n\tDescription: %s\n\tPrice: %s KWD" % (self.name, self.description, self.price)

class Cart(object):
    def __init__(self):
        """
        Initializes a new cart with an empty list of products.
        """
        # your code goes here!
        self.products = []

    def add_to_cart(self, product):
        """
        Adds a product to this cart.
        """
        # your code goes here!
        self.products.append(product)



    def get_total_price(self):
        """
        Returns the total price of all the products in this cart.
        """
        # your code goes here!
        total = 0
        for items in self.products:
            total += product.price
        return total


    def print_receipt(self):
        """
        Prints the receipt in a nice readable format.
        """
        # your code goes here!
        print("Here is your receipt: ")
        for items in self.products:
            print(items)
            print("\t%s KWD" % product.price)
        print("Your total price is: %s KWD." % self.get_total_price())

    def checkout(self):
        """
        Does the checkout.
        """
        # your code goes here!
        print("-------------------------------")
        self.print_receipt()
        confirmation = input("If you would like to confirm your order Type 'Y' and if you would like to cancel your order please type 'N' here: ")
        if confirmation.upper == "Y":
            print()
            print("Your order has been placed.")
        else:
            print()
            print("Your order has been cancelled.")

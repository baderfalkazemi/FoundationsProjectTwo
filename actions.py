# UTILS AND FUNCTIONALITY
from data import stores
from components import Cart

site_name = "www.bandk.com"  # Give your site a name

def welcome():
    print("Welcome to %s\nFeel free to shop throughout the stores we have, and only checkout once!" % site_name)

def print_stores():
    """
    prints the list of stores in a nice readable format.
    """
    # your code goes here!
    for shop in stores:
        print("- %s" % shop.name)

def get_store(store_name):
    """
    receives a name for a store, and returns the store object with that name.
    """
    # your code goes here!
    for shops in stores:
        if shops.name.lower() == store_name.lower():
            return shops
        else:
            return False

def pick_store():
    """
    prints list of stores and prompts user to pick a store.
    """
    # your code goes here!
    store_found = False
    while not store_found:
        print_stores()
        store_name = input("Pick a store by typing its name. Or type \"checkout\" to pay your bills and say your goodbyes.\n").lower()
        if store_name.lower() == "checkout":
            return "checkout"
        picked_store = get_store(store_name)
        if picked_store:
            break

        print("No store with that name. Please try again.")

    return picked_store

def pick_products(cart, picked_store):
    """
    prints list of products and prompts user to add products to cart.
    """
    # your code goes here!
    print("Pick the items you'd like to add in your cart by typing the product name exactly as it was spelled above.")
    print('Type \"back\" to go back to the main menu where you can checkout.')
    user_selected_products = ""
    while user_selected_products.lower() != "back":
        for product in picked_store.products:
            if user_selected_products.lower() == Product.name.lower():
                cart.add_to_cart(product)
        user_selected_products = input()
    return user_selected_products

def shop():
    """
    The main shopping functionality
    """
    cart = Cart()
    # your code goes here!
    user_input = ""
    while user_input.lower() != "checkout":
        user_input = ""
        picked_store = pick_store()
        if picked_store == "checkout":
            break

        picked_store.print_products()
        user_input = pick_products(cart, picked_store)

    cart.checkout()


def thank_you():
    print("Thank you for shopping with us at %s" % site_name)

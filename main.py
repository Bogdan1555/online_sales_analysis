from product import Product
from product_manager import ProductManager

if __name__ == "__main__":
    manager = ProductManager()

    # Adăugați produse
    p1 = Product("Apple", 0.5, 10)
    p2 = Product("Banana", 0.3, 15)
    p3 = Product("Orange", 0.7, 8)

    manager.add_product(p1)
    manager.add_product(p2)
    manager.add_product(p3)

    # Afișați produsele și valoarea totală
    print(manager.display_products())
    print(f'Total Inventory Value: {manager.total_value()}')
    
from cart import Cart

if __name__ == "__main__":
    # ... (codul existent)

    cart = Cart()

    # Adăugați 3 produse în coș
    cart.add_to_cart(p1)
    cart.add_to_cart(p2)
    cart.add_to_cart(p3)

    # Afișați valoarea totală și produsele din coș
    print(f'Total Cart Value: {cart.total_cart_value()}')
    print(f'Cart Items: {cart.display_cart()}')
p2.update_quantity(20)  # Actualizați cantitatea pentru Banana

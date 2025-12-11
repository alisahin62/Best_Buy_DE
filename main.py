import store
import products

product_list = [ products.Product("MacBook Air M2", price=1450, quantity=100),
                 products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                 products.Product("Google Pixel 7", price=500, quantity=250)
               ]

best_buy = store.Store(product_list)



def list_products():
    product_no = 1
    for product in product_list:
        print(f"{product_no}. {product.name}, Price: {product.price}, Quantity: {product.quantity}")
        product_no += 1

def show_total_amount():
    total_items = 0
    for product in product_list:
        total_items += product.quantity
    print(f"Total of {total_items} items in store.")

def make_an_order():
    cart = []
    while True:
        list_products()
        product_no = input("""When you want to finish order, enter empty text.
Which product # do you want? """)

        if product_no == "":
            return cart

        if not product_no.isdigit():
            print("Please enter a valid number.")
            continue

        product_no = int(product_no)

        if 1 <= product_no <= len(product_list):
            while True:
                qty = input("What amount do you want?")
                if not qty.isdigit():
                    print("Please enter a valid number.")
                    continue
                qty = int(qty)
                if qty >= 1:
                    cart.append((product_list[product_no - 1], qty))
                    print("Product added to list.")
                    break
        else:
            print("Number out of range. Try again.")



def start():
    while True:
        user_choice = input("""   
Store Menu
----------
1. List all products in store
2. Show total amount in store
3. Make an order
4. Quit
Please choose a number:""")

        if user_choice == "1":
            list_products()

        elif user_choice == "2":
            show_total_amount()

        elif user_choice == "3":
            make_an_order()

        elif user_choice == "4":
            break
        else:
            print("Invalid Option.")


if __name__ == "__main__":
    start()
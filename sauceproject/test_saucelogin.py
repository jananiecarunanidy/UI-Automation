
from playwright.sync_api import Page, expect
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from pages.checkout_complete_page import CheckoutCompletePage


def test_saucelogin(page: Page):

    #Open application
    page.goto("https://www.saucedemo.com/")

#------------LOGIN PAGE-----------------#
    login_page = LoginPage(page)

    login_page.login("standard_user", "secret_sauce")

#------------INVENTORY PAGE-------------#
    inventory_page = InventoryPage(page)

    # Verify 6 products
    expect(inventory_page.product_names).to_have_count(6)
    print("No. of products:", inventory_page.get_product_count())

    # Verify product names
    print("Product names:", inventory_page.get_product_names())

    # Verify product prices
    print("Product prices:", inventory_page.get_product_prices())

    # Add products
    inventory_page.add_backpack()
    inventory_page.add_red_tshirt()

    # Sort products
    inventory_page.sort_products("az")
    print("A to Z:", inventory_page.get_sorted_product_names())

    inventory_page.sort_products("za")
    print("Z to A:", inventory_page.get_sorted_product_names())

    inventory_page.sort_products("lohi")
    print("Low to High:", inventory_page.get_sorted_product_prices())

    inventory_page.sort_products("hilo")
    print("High to Low:", inventory_page.get_sorted_product_prices())

    # Open cart
    inventory_page.open_cart()
    expect(page).to_have_url("https://www.saucedemo.com/cart.html")

 # ---------------- CART PAGE ----------------#
    cart_page = CartPage(page)

    # Verify cart has 2 products
    expect(cart_page.cart_items).to_have_count(2)

    print("No. of items in cart:",cart_page.get_cart_item_count())

    print("Products in cart:",cart_page.get_cart_product_names())

    # Go to checkout
    cart_page.click_checkout()

    expect(page).to_have_url("https://www.saucedemo.com/checkout-step-one.html")

 # --------------- CHECKOUT PAGE ----------------#

    checkout_page = CheckoutPage(page)

    #Enter checkout information
    checkout_page.enter_checkout_information("Teddy", "Bear", "605001")

    checkout_page.click_continue()

    expect(page).to_have_url("https://www.saucedemo.com/checkout-step-two.html")

    # Verify summary
    expect(checkout_page.get_payment_information()).to_contain_text("SauceCard")

    expect(checkout_page.get_shipping_information()).to_contain_text("Free")

    expect(checkout_page.get_total()).to_contain_text("Total")

    # Finish order
    checkout_page.finish_order()

 # ----------------- CHECKOUT COMPLETE PAGE -------------#

    checkout_complete_page = CheckoutCompletePage(page)

    # Verify order was successfully completed

    expect(page).to_have_url("https://www.saucedemo.com/checkout-complete.html")

    expect(checkout_complete_page.get_order_complete_message()).to_have_text("Thank you for your order!")

    # Back Home
    checkout_complete_page.click_back_home()

    expect(page).to_have_url("https://www.saucedemo.com/inventory.html")


    # Verify Logout
    checkout_complete_page.logout()

    expect(page).to_have_url("https://www.saucedemo.com/")

    page.wait_for_timeout(4000)



           




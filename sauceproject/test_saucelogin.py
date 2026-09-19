
from playwright.sync_api import Page, expect

#login page
def test_saucelogin(page:Page):
    page.goto("https://www.saucedemo.com/")
    page.locator("#user-name").fill("standard_user")
    page.locator("#password").fill("secret_sauce")
    page.locator("#login-button").click()

#Verify 6 products
    list=page.locator("div.inventory_item_name")
    expect(list).to_have_count(6)
    print(list.count())

#Verify product names
    productnames=page.locator("div.inventory_item_name")
    print(productnames.all_text_contents())

#Verify product prices
    productprices=page.locator("div.inventory_item_price")
    print(productprices.all_text_contents())

#Add products to the cart
    firstitem=page.locator("button[name='add-to-cart-sauce-labs-backpack']")
    firstitem.click()
    seconditem=page.locator("button[name='add-to-cart-test.allthethings()-t-shirt-(red)']")
    seconditem.click()

#Verify the cart
    page.locator(".shopping_cart_link").click()
    expect(page).to_have_url("https://www.saucedemo.com/cart.html")

#Verify 2 products are in the cart
    checkcartitems=page.locator(".cart_item")
    expect(checkcartitems).to_have_count(2)
    print("No.of items in cart", checkcartitems.count())

#Verify the product names
    cart_products = page.locator(".inventory_item_name")
    print("Products in cart:", cart_products.all_text_contents())

#Go back to inventory
    page.locator("#continue-shopping").click()
    expect(page).to_have_url("https://www.saucedemo.com/inventory.html")

#Product sorting names A to Z
    page.locator(".product_sort_container").select_option("az")
    inventorysort=page.locator(".inventory_item_name")
    print("Print Name(A to Z):", inventorysort.all_text_contents())
    expect(inventorysort.nth(0)).to_have_text("Sauce Labs Backpack")

#Product sorting names Z to A
    page.locator(".product_sort_container").select_option("za")
    inventorysort=page.locator(".inventory_item_name")
    print("Print Name(Z to A):", inventorysort.all_text_contents())
    expect(inventorysort.nth(0)).to_have_text("Test.allTheThings() T-Shirt (Red)")

#price sorting from low to high
    page.locator(".product_sort_container").select_option("lohi")
    pricesort=page.locator(".inventory_item_price")
    print("Print Price(low to high):", pricesort.all_text_contents())

#price sorting from high to low
    page.locator(".product_sort_container").select_option("hilo")
    pricesort=page.locator(".inventory_item_price")
    print("Print Price(high to low):", pricesort.all_text_contents())

#To check the product details
    page.locator("#item_4_img_link").click()
    expect(page).to_have_url("https://www.saucedemo.com/inventory-item.html?id=4")
    expect(page.locator(".inventory_details_name")).to_have_text("Sauce Labs Backpack")
    expect(page.locator(".inventory_details_price")).to_have_text("$29.99")
    page.go_back()
    page.locator("#item_3_img_link").click()
    expect(page.locator(".inventory_details_name")).to_have_text("Test.allTheThings() T-Shirt (Red)")
    expect(page.locator(".inventory_details_price")).to_have_text("$15.99")
    page.locator(".shopping_cart_link").click()
    expect(page).to_have_url("https://www.saucedemo.com/cart.html")

#Go to Cart and Checkout
    page.locator("#checkout").click()
    expect(page).to_have_url("https://www.saucedemo.com/checkout-step-one.html")

#Enter Checkout information
    page.get_by_placeholder("First Name").fill("Teddy")
    page.get_by_placeholder("Last Name").fill("Bear")
    page.get_by_placeholder("Zip/Postal Code").fill("605001")

    page.locator("#continue").click()
    expect(page).to_have_url("https://www.saucedemo.com/checkout-step-two.html")

#Summary Page details
    expect(page.locator(".summary_value_label").nth(0)).to_contain_text("SauceCard")
    expect(page.locator(".summary_value_label").nth(1)).to_contain_text("Free")
    expect(page.locator(".summary_total_label")).to_contain_text("Total")
    page.locator("#finish").click()


# verify that the order was successfully completed
    expect(page).to_have_url("https://www.saucedemo.com/checkout-complete.html")
    expect(page.locator(".complete-header")).to_have_text("Thank you for your order!")

#Verify the Back Home button
    page.locator("#back-to-products").click()
    expect(page).to_have_url("https://www.saucedemo.com/inventory.html")

#Verify logout
    page.locator("#react-burger-menu-btn").click()
    page.locator("#logout_sidebar_link").click()
    expect(page).to_have_url("https://www.saucedemo.com/")

    page.wait_for_timeout(4000)



           




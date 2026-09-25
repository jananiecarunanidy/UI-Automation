
from playwright.sync_api import Page

class InventoryPage:

    def __init__(self, page:Page):
        self.page = page

        #product details
        self.product_names = page.locator("div.inventory_item_name")
        self.product_prices = page.locator("div.inventory_item_price")

        #Add to cart
        self.backpack = page.locator("button[name='add-to-cart-sauce-labs-backpack']")
        self.red_tshirt = page.locator("button[name='add-to-cart-test.allthethings()-t-shirt-(red)']")

        #cart
        self.cart = page.locator(".shopping_cart_link")

        #sorting
        self.sort_dropdown = page.locator(".product_sort_container")

        #Product images
        self.backpack_image = page.locator("#item_4_img_link")
        self.red_tshirt_image = page.locator("#item_3_img_link")

    def get_product_count(self):
           return self.product_names.count()

    def get_product_names(self):
           return self.product_names.all_text_contents()

    def get_product_prices(self):
           return self.product_prices.all_text_contents()

    def add_backpack(self):
           self.backpack.click()

    def add_red_tshirt(self):
           self.red_tshirt.click()

    def open_cart(self):
            self.cart.click()

    def sort_products(self, option):
            self.sort_dropdown.select_option(option)

    def get_sorted_product_names(self):
           return self.product_names.all_text_contents()

    def get_sorted_product_prices(self):
           return self.product_prices.all_text_contents()

    def open_backpack_details(self):
            self.backpack_image.click()

    def open_red_tshirt_details(self):
            self.red_tshirt_image.click()






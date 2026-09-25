from playwright.sync_api import Page


class CartPage:

    def __init__(self, page: Page):
        self.page = page

        self.cart_items = page.locator(".cart_item")
        self.product_names = page.locator(".inventory_item_name")

        self.continue_shopping_button = page.locator("#continue-shopping")
        self.checkout_button = page.locator("#checkout")

    def get_cart_item_count(self):
        return self.cart_items.count()

    def get_cart_product_names(self):
        return self.product_names.all_text_contents()

    def continue_shopping(self):
        self.continue_shopping_button.click()

    def click_checkout(self):
        self.checkout_button.click()
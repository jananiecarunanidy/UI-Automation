
from playwright.sync_api import Page


class CheckoutCompletePage:

    def __init__(self, page: Page):
        self.page = page

        # Order completion message
        self.complete_header = page.locator(".complete-header")

        #Back Home button
        self.back_home_button = page.locator("#back-to-products")

        # Menu and Logout
        self.menu_button = page.locator("#react-burger-menu-btn")
        self.logout_button = page.locator("#logout_sidebar_link")

    def get_order_complete_message(self):
        return self.complete_header

    def click_back_home(self):
        self.back_home_button.click()

    def logout(self):
        self.menu_button.click()
        self.logout_button.click()
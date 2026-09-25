
from playwright.sync_api import Page

class CheckoutPage:

        def __init__(self, page: Page):
                self.page = page

                self.checkout = page.locator("#checkout")

                self.first_name = page.get_by_placeholder("First Name")
                self.last_name = page.get_by_placeholder("Last Name")
                self.zip_code = page.get_by_placeholder("Zip/Postal Code")
                self.continue_button = page.locator("#continue")


                self.summary_values = page.locator(".summary_value_label")
                self.summary_total = page.locator(".summary_total_label")
                self.finish_button = page.locator("#finish")


        def click_checkout(self):
               self.checkout.click()

        def enter_checkout_information(self, first_name, last_name, zip_code):
                self.first_name.fill(first_name)
                self.last_name.fill(last_name)
                self.zip_code.fill(zip_code)

        def click_continue(self):
                self.continue_button.click()

        def get_payment_information(self):
               return self.summary_values.nth(0)

        def get_shipping_information(self):
               return self.summary_values.nth(1)

        def get_total(self):
               return self.summary_total

        def finish_order(self):
               self.finish_button.click()


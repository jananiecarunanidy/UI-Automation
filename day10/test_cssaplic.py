
from playwright.sync_api import Page, expect

def test_css_check(page:Page):
    page.goto("https://demowebshop.tricentis.com/")


    page.locator("img[alt='Tricentis Demo Web Shop']")


    page.locator("input#small-searchterms").fill("computer")
    page.locator("input[type='submit']").click()
    page.get_by_role('combobox',)


    products = page.locator('h2 > a[href*="computer"]')
    expect(products).to_have_count(4)
    print(products.count())

    print("First product:", products.first.text_content())
    print("Last product:", products.last.text_content())
    print("Third product:", products.nth(2).text_content())

    print("All products:", products.all_text_contents())

    links = page.locator("div.column.follow-us ul li a")
    print(links.first.text_content())
    print(links.last.text_content())
    print(links.nth(2).text_content())
    page.wait_for_timeout(4000)
    







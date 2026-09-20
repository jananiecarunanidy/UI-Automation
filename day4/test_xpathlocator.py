
from playwright.sync_api import Page, expect

def test_xpath_locators(page: Page):
    page.goto("https://demowebshop.tricentis.com/")

    expect(page.locator("//html/body/div[4]/div[1]/div[1]/div[1]/a/img")).to_be_visible()
    expect(page.locator("//img[@alt='Tricentis Demo Web Shop']")).to_be_visible()

    page.wait_for_timeout(5000)

    products=page.locator("//h2//a[contains(@href,'computer')]")
    print("Products count:", products.count())
    expect(products).to_have_count(4)

    print("First computer product:", products.first.text_content())
    print("Last computer product:", products.last.text_content())
    print("N-th computer product:", products.nth(2).text_content())

    product_titles=products.all_text_contents()
    print("Product titles:", product_titles)

    print("Printing product titles using loop statement")
    for i in product_titles:
        print(i)

    building_products=page.locator("//h2//a[starts-with(@href,'/build')]")
    print("Count of building products:", building_products.count())
    expect(building_products).to_have_count(building_products.count())

    registration_link=page.locator("//a[text()='Register']")
    expect(registration_link).to_be_visible


    googlepluslink=page.locator("//div[@class='column follow-us']//li[last()]")
    expect(googlepluslink).to_have_text("Google+")

    twitterlink=page.locator("//div[@class='column follow-us']//li[position()=2]")
    expect(twitterlink).to_have_text("Twitter")

    




    







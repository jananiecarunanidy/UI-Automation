
from playwright.sync_api import Page, expect

def test_rahulpracttise(page:Page):
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")
    page.locator("label[for='username']").fill("rahulshettyacademy")
    page.locator("label[for='password']").fill("Learning@830$3mK2")
    page.locator("input[type='radio'][value='user']").check()
    page.locator("select").select_option("Student")
    page.locator("input#signInBtn").click()


def test_add_product(page:Page):
    page.goto("https://rahulshettyacademy.com/angularpractice/shop")
    iphoneProduct=page.locator("app-card").filter(has_text="iphone X") 
    iphoneProduct.get_by_role("button").click()
    nokiaProduct=page.locator("app-card").filter(has_text="Nokia Edge")
    nokiaProduct.get_by_role("button").click()
    page.get_by_text("Checkout").click() 
    product1 = page.locator("(//h4[@class='media-heading'])")
    expect(product1).to_have_count(2)
    print("First product:", product1.first.text_content())
    print("Second product:", product1.nth(1).text_content())

def test_childWindow(page:Page):
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")
    page.get_by_role("link", name="Free Access to InterviewQues/ResumeAssistance/Material").click()
    

    



    page.wait_for_timeout(3000)













from playwright.sync_api import Page, expect

def test_login(page:Page):
    page.goto("https://automationexercise.com/login")
    expect(page.get_by_role("heading",name="Login to your account")).to_be_visible()

    page.get_by_placeholder("Email Address").nth(0).fill("bluejansha93@gmail.com")
    page.get_by_placeholder("Password").fill("password123")
    page.get_by_role("button",name="Login").click()

    page.wait_for_timeout(5000)

def test_signup(page:Page):
    page.goto("https://automationexercise.com/login")
    expect(page.get_by_role("heading",name="New User Signup!")).to_be_visible()
    page.get_by_placeholder("Name").fill("jananie")
    page.get_by_placeholder("Email Address").nth(1).fill("bluejanshat931219@gmail.com")
    page.get_by_role("button",name="Signup").click()

    expect(page.get_by_text("Enter Account Information")).to_be_visible()
    #Select Title
    #page.check("#id_gender1")
    page.check("#id_gender2")
    page.locator("#password").fill("password123")
    page.select_option("select[name='days']","10")
    page.select_option("select[name='months']","April")
    page.select_option("select[name='years']","1990")

    expect(page.get_by_text("Address Information")).to_be_visible()
    page.locator("#first_name").fill("jananie")
    page.locator("#last_name").fill("C")
    page.locator("#company").fill("xyz")
    page.locator("#address1").fill("No:12,Sri Ram")
    page.locator("#address2").fill("Appartment")
    page.select_option("select[name='country']","Israel")
    page.locator("#state").fill("Haifa")
    page.locator("#city").fill("Israel")
    page.locator("#zipcode").fill("1232456")
    page.locator("#mobile_number").fill("999999999")
    page.get_by_role("button",name='Create Account').click()
    page.get_by_role("link", name="Continue").click()

 



      

    page.wait_for_timeout(5000)



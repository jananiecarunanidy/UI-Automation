

from playwright.sync_api import Page, expect

def test_multi_select_dropdown(page:Page):
    page.goto("https://testautomationpractice.blogspot.com/")
    #page.locator("#colors").select_option(label=["Red","Blue","Green"])
    #page.locator("#colors").select_option(value=["red","blue","green"])
    #page.locator("#colors").select_option(index=[2,4])

    dropdown_options=page.locator("#colors>option")
    expect(dropdown_options).to_have_count(7)
    page.wait_for_timeout(5000)

    




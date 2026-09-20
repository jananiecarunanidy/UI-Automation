
from playwright.sync_api import Page, expect

def test_inputbox(page:Page):
    page.goto("https://testautomationpractice.blogspot.com/")


    male_radio=page.locator("#male")

    expect(male_radio).to_be_visible()
    expect(male_radio).to_be_enabled()

    expect(male_radio).not_to_be_checked()

    male_radio.check()

    expect(male_radio).to_be_checked()

    page.wait_for_timeout(1000)


    
    female_radio=page.locator("#female")

    expect(female_radio).to_be_visible()
    expect(female_radio).to_be_enabled()

    expect(female_radio).not_to_be_checked()

    female_radio.check()

    expect(female_radio).to_be_checked()

    page.wait_for_timeout(1000)
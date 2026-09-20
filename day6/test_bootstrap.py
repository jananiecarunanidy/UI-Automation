from playwright.sync_api import Page, expect

def test_bootstrap_dropdown(page:Page):
    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

    page.get_by_placeholder("Username").fill("Admin")
    page.get_by_placeholder("Password").fill("admin123")
    page.get_by_role("button", name='Login').click()

    page.get_by_text('PIM').click()


    page.locator("form i").nth(2).click()
    page.wait_for_timeout(3000)
    options=page.locator("div[role='listbox'] span")
    count=options.count()
    print("Number of options in the dropdown:", count)
    expect(options).to_have_count(count)   

    page.wait_for_timeout(2000)
    print("All option from the dropdown",options.all_text_contents())




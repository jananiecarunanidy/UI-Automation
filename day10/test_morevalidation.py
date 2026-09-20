
from playwright.sync_api import Page, expect

def test_UIChecks(page:Page):
    page.goto("https://rahulshettyacademy.com/AutomationPractice/")
    expect(page.get_by_placeholder("Hide/Show Example")).to_be_visible()
    page.get_by_role("button", name="Hide").click()
    expect(page.get_by_placeholder("Hide/Show Example")).to_be_hidden()

    page.on("dialog", lambda dialog: dialog.accept())
    page.get_by_role("button", name="Confirm").click()
    pageFrame=page.frame_locator("#courses-iframe")
    pageFrame.get_by_role("link", name="All Access Plan").click()
    expect(pageFrame.locator("body")).to_contain_text(" Learn Earn & Shine")

    page.goto("https://rahulshettyacademy.com/seleniumPractise/#/offers")
    for index in range(page.locator("th").count()):
        if page.locator("th").nth(index).filter(has_text="Price").count()>0:
         colvalue = index
         print(f"Price column value is {colvalue}")
         break
    riceRow = page.locator("tr").filter(has_text="Rice")
    expect(riceRow.locator("td").nth(colvalue)).to_have_text("37")
    print("Rice row value is:", riceRow.locator("td").nth(colvalue).text_content())




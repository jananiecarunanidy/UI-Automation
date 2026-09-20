
from playwright.sync_api import Page, expect

def test_login(page: Page):
    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

    page.get_by_placeholder("Username").fill("Admin")
    page.get_by_placeholder("Password").fill("admin123")

    page.get_by_role("button", name='Login').click()

    expect(page).to_have_url("https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index")

    expect(page.get_by_text("Dashboard",exact=True)).to_be_visible
        # Dashboard sections
    expect(page.get_by_text("Time at Work", exact=True)).to_be_visible()
    expect(page.get_by_text("My Actions", exact=True)).to_be_visible()
    expect(page.get_by_text("Quick Launch", exact=True)).to_be_visible()

    expect(page.get_by_text("Admin", exact=True)).to_be_visible()
    expect(page.get_by_text("PIM", exact=True)).to_be_visible()
    expect(page.get_by_text("Leave", exact=True)).to_be_visible()

    page.wait_for_timeout(30000)
from playwright.sync_api import Page, expect

def test_verify_pwlocators(page: Page):

    page.goto("https://www.toolsqa.com/selenium-training/")

    # 1. get_by_alt_text()
    logo = page.get_by_alt_text("Tools QA", exact=True)
    expect(logo).to_be_visible()

    # 2. get_by_text()
    expect(
        page.get_by_text(
            "To register for Paid Training, please fill out form below:",
            exact=True
        )
    ).to_be_visible()

    # 3. get_by_role()
    expect(
        page.get_by_role("button", name="Send")
    ).to_be_visible()

    page.get_by_label("First Name (required)").fill("Jananie")
    page.get_by_label("Last Name").fill("C")
    page.get_by_label("Email (required)").fill("test@gmail.com")
    page.get_by_label("Mobile (required)").fill("9876543210")
    page.get_by_label("City (required)").fill("Pondicherry")
    page.get_by_label("Your Message (required)").fill("its my message")
    page.get_by_label("Input this code").fill("ULcd")
    page.wait_for_timeout(10000)

    page.get_by_placeholder("Search").first.fill("Java")
    
    page.wait_for_timeout(30000)


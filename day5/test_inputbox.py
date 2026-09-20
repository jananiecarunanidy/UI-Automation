

from playwright.sync_api import Page, expect

def test_inputbox(page:Page):
    page.goto("https://testautomationpractice.blogspot.com/")

    text_box=page.locator("#name")

    expect(text_box).to_be_visible()
    expect(text_box).to_be_enabled()

    expect(text_box).to_have_attribute("maxlength","15")

    maxlength=text_box.get_attribute("maxlength")
    print("Maximum length of inputbox:", maxlength)

    text_box.fill("John Kennedy")

    enteredvalue=text_box.input_value()
    print("Value entered is:", enteredvalue)

    page.wait_for_timeout(1000)

    email_box=page.locator("#email")
    expect(email_box).to_be_visible()
    expect(email_box).to_be_enabled()

    expect(email_box).to_have_attribute("maxlength","25")
    maxlength=email_box.get_attribute("maxlength")
    print("Maximum length of emailbox:", maxlength)


    email_box.fill("johnkennedy@gmail.com")

    enteredemailvalue=email_box.input_value()
    print("Value entered is:", enteredemailvalue)

    page.wait_for_timeout(1000)

    phone_box=page.locator("#phone")
    expect(phone_box).to_be_visible()
    expect(phone_box).to_be_enabled()

    expect(phone_box).to_have_attribute("maxlength","10")
    maxlength=phone_box.get_attribute("maxlength")
    print("Maximum length of phonebox:", maxlength)

    phone_box.fill("9999999999")

    enteredphonevalue=phone_box.input_value()
    print("Value entered is:", enteredphonevalue)

    page.wait_for_timeout(1000)

    address_box = page.locator("#textarea")

    expect(address_box).to_be_visible()
    expect(address_box).to_be_enabled()

    address_box.fill("123 Main Street, Chennai")

    enteredvalue = address_box.input_value()
    print("Address entered is:", enteredvalue)

    page.wait_for_timeout(1000)

    female_radio=page.locator("#female")
    
    expect(female_radio).to_be_visible()
    expect(female_radio).to_be_enabled()
    
    expect(female_radio).not_to_be_checked()
    
    female_radio.check()
    
    expect(female_radio).to_be_checked()
    
    page.wait_for_timeout(1000)

    days=['Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday']
    checkboxes=[]
    checkboxes=[page.get_by_label(day) for day in days]
    print("total number of checkboxes:", len(checkboxes))  

    
    weekdays="Friday"

    for label in days:
        if label==weekdays:
            checkbox=page.get_by_label(label)
            checkbox.check()
            expect(checkbox).to_be_checked()

    page.wait_for_timeout(2000)
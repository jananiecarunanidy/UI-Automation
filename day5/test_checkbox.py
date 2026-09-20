

from playwright.sync_api import Page, expect

def test_checkbox(page:Page):
    page.goto("https://testautomationpractice.blogspot.com/")


    # sunday_checkbox=page.get_by_label("Sunday")
    # sunday_checkbox.check()
    # expect(sunday_checkbox).to_be_checked()
    # page.wait_for_timeout(1000)

    days=['Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday']
    checkboxes=[]
    checkboxes=[page.get_by_label(day) for day in days]
    print("total number of checkboxes:", len(checkboxes))

    # for checkbox in checkboxes:
    #     checkbox.check()
    #     expect(checkbox).to_be_checked()

    # page.wait_for_timeout(2000)

    # for checkbox in checkboxes[-3:]:
    #      checkbox.uncheck()
    #      expect(checkbox).not_to_be_checked()
    
    # page.wait_for_timeout(2000)


    # indexes= [1,3,6]

    # for i in indexes:
    #     checkboxes[i].check()
    #     expect(checkboxes[i]).to_be_checked()

    # page.wait_for_timeout(2000)

    weekdays="Friday"

    for label in days:
        if label==weekdays:
            checkbox=page.get_by_label(label)
            checkbox.check()
            expect(checkbox).to_be_checked()

    page.wait_for_timeout(2000)

    

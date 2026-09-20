import pytest
from playwright.sync_api import Page, expect

def select_date(page, target_year, target_month, target_date, is_future):
    while True:
        current_month = page.locator('.ui-datepicker-month').text_content().strip()
        current_year = page.locator('.ui-datepicker-year').text_content().strip()

        if current_month==target_month and current_year==target_year:
            break
        if is_future==False:
            page.locator(".ui-datepicker-next").click()
        else:
            page.locator(".ui-datepicker-prev").click()

    all_dates=page.locator(".ui-datepicker-calendar td").all()

    for dt in all_dates:
        date_text=dt.inner_text()
        if(date_text==target_date):
            dt.click()

def test_jquery_datepicker(page:Page):
    page.goto("https://testautomationpractice.blogspot.com/")

    date_input=page.locator("#datepicker")

    # date_input.fill("10/15/2025")

    is_future = True
    year = "2024"
    month = "October"
    date = "15"
    date_input.click()
    select_date(page, year, month, date, is_future)
    expect(date_input).to_have_value("10/15/2024")

    page.wait_for_timeout(5000)





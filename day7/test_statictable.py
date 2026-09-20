from playwright.sync_api import Page, expect

def test_login(page: Page):
    page.goto("https://testautomationpractice.blogspot.com/")


    table=page.locator("table[name='BookTable'] tbody")
    expect(table).to_be_visible()
    rows=page.locator("table[name='BookTable'] tbody tr")
    expect(rows).to_have_count(7)

    row_count=rows.count()
    print("Number of rows in a table:", row_count)

    columns=rows.locator("th")
    expect(columns).to_have_count(4)

    column_count=columns.count()
    print("Number of columns in a table:",column_count)

    second_row_cells=rows.nth(2).locator('td')
    second_row_texts=second_row_cells.all_inner_texts()
    print("2nd row data:", second_row_texts)

    expect(second_row_cells).to_have_text(['Learn Java', 'Mukesh', 'Java', '500'])
    for text in second_row_texts:
        print(text)


    all_row_data=rows.all()
    # for row in all_row_data[1:]:
    #     cols=row.locator('td').all_inner_texts()
    #     print(cols)


    for row in all_row_data[1:]:
        author_name=row.locator('td').nth(1).inner_text()
        if author_name=='Mukesh':
                book_name=row.locator('td').nth(0).inner_text()
                print(f"{author_name} \t {book_name}")

    total_price=0
    for row in all_row_data[1:]:
         price=row.locator('td').nth(3).inner_text()
         total_price=total_price+int(price)

    print("Total price:",total_price)

    page.wait_for_timeout(1000)
    



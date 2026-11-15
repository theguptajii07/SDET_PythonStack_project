import re

from playwright.sync_api import Page, expect

def test_login_with_valid_credentials_shows_products(page: Page):
    #Arrange: open the login page
    page.goto("https://www.saucedemo.com/")

    #Act: log in as the standard test user
    page.get_by_placeholder("Username").fill("standard_user")
    page.get_by_placeholder("Password").fill("secret_sauce")
    page.get_by_role("button", name="Login").click()

    #Assert: we reached the inventory page and it shows the Products title
    expect(page).to_have_url(re.compile(r".*/inventory\.html"))
    expect(page.get_by_text("Products", exact=True)).to_be_visible()
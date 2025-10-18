import os
from playwright.sync_api import sync_playwright

proxy = {
    "server": "brd.superproxy.io:33335",
    "username": "brd-customer-hl_8d2f0e58-zone-web_unlocker1",
    "password": "b9x8stq3iyo0"
}

pw = sync_playwright().start()

browser = pw.chromium.launch(headless=False, slow_mo=2000, proxy=proxy)

page = browser.new_page()

# page.goto("http://geektime.co.il/", timeout=90000)
page.goto("http://walmart.com")

# locate search input
page.locator("xpath=//input[@aria-label='Search']").fill("testing")
# submit search term
page.keyboard.press('Enter');


browser.close()
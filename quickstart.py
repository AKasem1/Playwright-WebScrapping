import os
from playwright.sync_api import sync_playwright
from urllib.request import urlretrieve

pw = sync_playwright().start()

browser = pw.chromium.launch(headless=False, slow_mo=2000)

page = browser.new_page()
page.goto("https://arxiv.org/search")

page.get_by_placeholder("Search term...").fill("quantum computing")

page.get_by_role("button").get_by_text("Search").nth(1).click()

links = page.locator("xpath=//a[contains(@href, 'arxiv.org/pdf')]").all()

output_dir = "data"
os.makedirs(output_dir, exist_ok=True)

for link in links:
    url = link.get_attribute("href")
    urlretrieve(url, "data/" + url[-5:] + ".pdf")

print(page.title())
page.screenshot(path="arxiv_search.png")


browser.close()
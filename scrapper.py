from playwright.sync_api import sync_playwright, Playwright, Browser

class Scrapper():
  playwright: Playwright
  browser: Browser

  def __init__(self):
    self.playwright = sync_playwright().start()
    self.browser = self.playwright.chromium.launch()

  def __exit__(self):
    self.playwright.close()
    self.browser.stop()

  def scrape(self, URL: str):
    page = self.browser.new_page()
    page.goto(URL)

    for accordion in page.locator(".accordion-card-header").all():
      accordion.click()
      page.wait_for_timeout(2000)

    source = page.locator("main").inner_html()
    return source
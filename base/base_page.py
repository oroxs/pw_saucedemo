class BasePage:
    def __init__(self, page):
        self.page = page

    def goto(self, url):
        self.page.goto(url)

    def fill(self, selector, value):
        self.page.fill(selector, value)

    def click(self, selector):
        self.page.click(selector)

    def is_visible(self, selector):
        return self.page.is_visible(selector)

    def get_text(self, selector):
        return self.page.text_content(selector)

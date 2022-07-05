from pages.base import WebPage
from pages.elements import WebElement, ManyWebElements


class GoogleSearchPage(WebPage):

    def __init__(self, web_driver, url=''):
        url = 'https://google.com'
        super().__init__(web_driver, url)

    search_input = WebElement(css_selector='.gLFyf.gsfi')
    search_button = WebElement(class_name='gNO89b')
    result_stats = WebElement(id='result-stats')

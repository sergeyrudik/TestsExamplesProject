#!/usr/bin/python3
# -*- encoding=utf8 -*-

import pytest

from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture
def web_browser():
    options = Options()

    options.add_argument('--no-sandbox')
    options.add_argument('--log-level=DEBUG')
    options.add_argument("--start-maximized")
    chromedriver_path = r''

    browser = webdriver.Chrome(executable_path=chromedriver_path,
                               chrome_options=options)

    # Return browser instance to test case:
    yield browser

    browser.quit()

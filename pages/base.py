#!/usr/bin/python3
# -*- encoding=utf8 -*-

from termcolor import colored


class WebPage(object):
    _web_driver = None

    def __init__(self, web_driver, url=''):
        self._web_driver = web_driver
        self.get(url)

    def __setattr__(self, name, value):
        if not name.startswith('_'):
            self.__getattribute__(name)._set_value(self._web_driver, value)
        else:
            super(WebPage, self).__setattr__(name, value)

    def __getattribute__(self, item):
        attr = object.__getattribute__(self, item)

        if not item.startswith('_') and not callable(attr):
            attr._web_driver = self._web_driver
            attr._page = self

        return attr

    def get(self, url):
        self._web_driver.get(url)

    def switch_to_window(self, window_number):
        """ Switch to window"""
        self._web_driver.switch_to.window(self._web_driver.window_handles[window_number])

    def go_back(self):
        self._web_driver.back()

    def refresh(self):
        self._web_driver.refresh()

    def screenshot(self, file_name='screenshot.png'):
        self._web_driver.save_screenshot(file_name)

    def scroll_down(self, offset=0):
        """ Scroll the page down. """

        if offset:
            self._web_driver.execute_script('window.scrollTo(0, {0});'.format(offset))
        else:
            self._web_driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')

    def scroll_up(self, offset=0):
        """ Scroll the page up. """

        if offset:
            self._web_driver.execute_script('window.scrollTo(0, -{0});'.format(offset))
        else:
            self._web_driver.execute_script('window.scrollTo(0, -document.body.scrollHeight);')

    def switch_to_iframe(self, iframe):
        """ Switch to iframe by it's name. """

        self._web_driver.switch_to.frame(iframe)

    def switch_out_iframe(self):
        """ Cancel iframe focus. """
        self._web_driver.switch_to.default_content()

    def get_current_url(self):
        """ Returns current browser URL. """

        return self._web_driver.current_url

    def get_page_source(self):
        """ Returns current page body. """

        source = self._web_driver.page_source

        return source

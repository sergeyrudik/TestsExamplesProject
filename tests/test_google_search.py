from pages.google import GoogleSearchPage


class TestGoogleSearch:

    def test_base_page_open(self, web_browser):
        base_google_url = 'https://www.google.com/'

        page = GoogleSearchPage(web_browser)
        assert page.get_current_url() == base_google_url

    def test_base_search(self, web_browser):
        base_google_url = 'https://www.google.com/'

        page = GoogleSearchPage(web_browser)
        assert page.get_current_url() == base_google_url

        page.search_input.send_keys('google')
        page.search_button.click()

        assert page.get_current_url() != base_google_url
        assert 'search' in page.get_current_url()

        result_stats_with_text = (page.result_stats.get_text())[:-13]
        result_stats_without_text = ''.join(filter(str.isdigit, result_stats_with_text))

        print(result_stats_without_text)
        assert result_stats_without_text != ''
        assert result_stats_without_text > '1000'

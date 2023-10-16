import requests
from lxml import html


class ScrapeURL:
    def __init__(self, url):
        self.url = url
        self.html_elem = self.scrape()

    def scrape(self):
        response = requests.get(self.url)
        source = response.content
        html_elem = html.document_fromstring(source)
        return html_elem

    def get_page(self):
        return self.html_elem

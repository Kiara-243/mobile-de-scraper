thonpython
import logging
import requests
from parsers.listing_parser import ListingParser
from parsers.dealer_parser import DealerParser
from bs4 import BeautifulSoup

class DetailsExtractor:
    def __init__(self, settings):
        self.settings = settings
        self.listing_parser = ListingParser()
        self.dealer_parser = DealerParser()

    def extract(self, url):
        logging.info(f"Fetching details page: {url}")
        response = requests.get(url, headers=self.settings["headers"])
        response.raise_for_status()

        html = response.text
        listing = self.listing_parser.parse_full_listing(html)

        soup = BeautifulSoup(html, "html.parser")
        dealer_section = soup.select_one(".dealer-info")

        dealer_html = str(dealer_section) if dealer_section else html
        dealer = self.dealer_parser.parse(dealer_html)

        listing["dealerDetails"] = dealer
        return listing
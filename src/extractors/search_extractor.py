thonpython
import logging
import requests
from bs4 import BeautifulSoup
from parsers.listing_parser import ListingParser

class SearchExtractor:
    def __init__(self, settings):
        self.settings = settings
        self.parser = ListingParser()

    def extract(self, url):
        logging.info(f"Fetching search page: {url}")
        response = requests.get(url, headers=self.settings["headers"])
        response.raise_for_status()

        soup = BeautifulSoup(response.text, "html.parser")
        cards = soup.select(".listing")

        results = []
        for card in cards:
            item = self.parser.parse_listing_card(str(card))
            if item:
                results.append(item)

        logging.info(f"Extracted {len(results)} listings")
        return results
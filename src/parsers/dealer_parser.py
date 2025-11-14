thonpython
from bs4 import BeautifulSoup
from .utils import clean_text, extract_json_ld

class DealerParser:
    def parse(self, html):
        soup = BeautifulSoup(html, "html.parser")
        data = extract_json_ld(soup)

        dealer = data.get("seller", {})
        name = dealer.get("name")
        rating = dealer.get("aggregateRating", {}).get("ratingValue")
        country = dealer.get("address", {}).get("addressCountry")

        return {
            "name": name,
            "score": {"total": rating},
            "country": country
        }
thonpython
from bs4 import BeautifulSoup
import logging
from .utils import clean_text, extract_json_ld

class ListingParser:
    def parse_listing_card(self, html):
        soup = BeautifulSoup(html, "html.parser")

        try:
            title = clean_text(soup.select_one("h2.listing-title").text)
        except:
            title = None

        link_element = soup.select_one("a")
        url = link_element["href"] if link_element else None

        price_element = soup.select_one(".price-block")
        price = clean_text(price_element.text) if price_element else None

        image_el = soup.select_one("img")
        preview = image_el["src"] if image_el else None

        return {
            "title": title,
            "url": url,
            "previewImage": preview,
            "price": price
        }

    def parse_full_listing(self, html):
        soup = BeautifulSoup(html, "html.parser")
        data = extract_json_ld(soup)

        title = data.get("name")
        images = data.get("image", [])
        price = data.get("offers", {}).get("price")
        currency = data.get("offers", {}).get("priceCurrency")
        description = data.get("description")
        attributes = data.get("vehicleConfiguration", {})

        return {
            "title": title,
            "images": images,
            "price": {"amount": price, "currency": currency},
            "description": description,
            "attributes": attributes
        }
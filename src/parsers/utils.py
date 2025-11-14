thonpython
import json
import logging

def clean_text(text: str):
    if not text:
        return None
    return " ".join(text.strip().split())

def extract_json_ld(soup):
    json_ld = soup.find("script", type="application/ld+json")
    if not json_ld:
        return {}
    try:
        return json.loads(json_ld.text)
    except Exception as e:
        logging.error(f"Failed parsing JSON-LD: {e}")
        return {}
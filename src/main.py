thonpython
import json
import logging
from pathlib import Path
from extractors.search_extractor import SearchExtractor
from extractors.details_extractor import DetailsExtractor
from config.settings import load_settings

logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")

def run():
    settings = load_settings()
    input_file = Path("data/input.sample.json")

    if not input_file.exists():
        raise FileNotFoundError("data/input.sample.json not found")

    with open(input_file, "r", encoding="utf-8") as f:
        data = json.load(f)

    mode = data.get("mode")
    url = data.get("url")

    if mode == "search":
        extractor = SearchExtractor(settings)
        results = extractor.extract(url)
    elif mode == "details":
        extractor = DetailsExtractor(settings)
        results = extractor.extract(url)
    else:
        raise ValueError("Invalid mode. Must be 'search' or 'details'.")

    output_file = Path("data/sample_output.json")
    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(results, f, indent=2, ensure_ascii=False)

    logging.info(f"Extraction complete → {output_file}")

if __name__ == "__main__":
    run()
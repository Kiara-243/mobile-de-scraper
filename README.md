# 🔍🚗 Mobile.de Scraper

> A high-performance tool for extracting detailed vehicle listings from Mobile.de, including pricing, specifications, dealer information, images, and reviews.
> This scraper solves the challenge of collecting reliable, structured automotive data at scale for research, pricing analysis, and inventory intelligence.


<p align="center">
  <a href="https://bitbash.dev" target="_blank">
    <img src="https://github.com/za2122/footer-section/blob/main/media/scraper.png" alt="Bitbash Banner" width="100%"></a>
</p>
<p align="center">
  <a href="https://t.me/devpilot1" target="_blank">
    <img src="https://img.shields.io/badge/Chat%20on-Telegram-2CA5E0?style=for-the-badge&logo=telegram&logoColor=white" alt="Telegram">
  </a>&nbsp;
  <a href="https://wa.me/923249868488?text=Hi%20BitBash%2C%20I'm%20interested%20in%20automation." target="_blank">
    <img src="https://img.shields.io/badge/Chat-WhatsApp-25D366?style=for-the-badge&logo=whatsapp&logoColor=white" alt="WhatsApp">
  </a>&nbsp;
  <a href="mailto:sale@bitbash.dev" target="_blank">
    <img src="https://img.shields.io/badge/Email-sale@bitbash.dev-EA4335?style=for-the-badge&logo=gmail&logoColor=white" alt="Gmail">
  </a>&nbsp;
  <a href="https://bitbash.dev" target="_blank">
    <img src="https://img.shields.io/badge/Visit-Website-007BFF?style=for-the-badge&logo=google-chrome&logoColor=white" alt="Website">
  </a>
</p>




<p align="center" style="font-weight:600; margin-top:8px; margin-bottom:8px;">
  Created by Bitbash, built to showcase our approach to Scraping and Automation!<br>
  If you are looking for <strong>🔍🚗 Mobile.de Scraper</strong> you've just found your team — Let’s Chat. 👆👆
</p>


## Introduction

The **Mobile.de Scraper** automates collection of vehicle listings from Europe’s largest automotive marketplace. It enables businesses, analysts, and developers to access structured data on cars, motorcycles, and commercial vehicles.

### Why Vehicle Data Matters

- Helps businesses analyze market trends and pricing movements.
- Supports dealerships in building competitive and accurately priced inventories.
- Enables researchers to study depreciation, availability, and demand.
- Provides structured data for financial institutions, insurers, and automotive apps.
- Saves time by automating large-scale data collection.

## Features

| Feature | Description |
|--------|-------------|
| URL-based search | Use any Mobile.de search results URL to extract matching listings. |
| Listing URL scraping | Retrieve full details for individual listings instantly. |
| Configurable filters | Fine-tune search by mileage, model, registration year, power, sorting, and more. |
| Fast extraction | Processes up to ~4 results per second for high throughput. |
| Cost-efficient | Designed for large-scale extraction at minimal cost. |
| Multi-format export | Supports JSON, CSV, Excel, and other structured formats. |
| Detailed dealer insights | Extracts dealer reviews, ratings, contact info, and reputation metrics. |
| New price rating | Includes price evaluation ranges and labels. |

---

## What Data This Scraper Extracts

| Field Name | Field Description |
|------------|------------------|
| title | Listing title summarizing the vehicle. |
| previewImage | Main image URL of the listing. |
| brand | Vehicle manufacturer. |
| model | Vehicle model name. |
| url | Direct URL to the listing details. |
| price | Structured breakdown of price, currency, and pricing type. |
| description | Full vehicle description and feature notes. |
| attributes | Key vehicle specifications such as mileage, fuel type, engine size, seats, transmission, and more. |
| features | List of vehicle features and equipment. |
| images | Array of URLs linking to all listing images. |
| dealerDetails | Seller information, ratings, languages, location, and reviews. |
| priceRating | Price evaluation label and ranges. |
| createdDate | When the listing was first posted. |
| modifiedDate | Latest update timestamp. |
| renewedDate | Last refreshed timestamp. |

---

## Example Output


    {
      "title": "Audi A5 Sportback 2.0 TFSI*S-LINE*XENON*SH*LED*NAVI*",
      "segment": "Car",
      "brand": "Audi",
      "model": "A5",
      "url": "https://suchen.mobile.de/fahrzeuge/details.html?id=413683625",
      "price": {
        "total": { "amount": 19990, "currency": "EUR" },
        "type": "FIXED"
      },
      "attributes": {
        "Mileage": "89,106 km",
        "Power": "169 kW (230 hp)",
        "Fuel": "Petrol",
        "Emission Class": "Euro6",
        "Transmission": "Automatic"
      },
      "dealerDetails": {
        "name": "Autohaus West Rheinland",
        "score": { "total": 4.9 },
        "country": "DE"
      }
    }

---

## Directory Structure Tree


    🔍🚗 Mobile.de Scraper/
    ├── src/
    │   ├── main.py
    │   ├── parsers/
    │   │   ├── listing_parser.py
    │   │   ├── dealer_parser.py
    │   │   └── utils.py
    │   ├── extractors/
    │   │   ├── search_extractor.py
    │   │   └── details_extractor.py
    │   └── config/
    │       └── settings.example.json
    ├── data/
    │   ├── input.sample.json
    │   └── sample_output.json
    ├── requirements.txt
    └── README.md

---

## Use Cases

- **Dealerships** use it to analyze competitor pricing and supply data so they can optimize their inventory strategy.
- **Market analysts** extract large datasets to study regional pricing trends and demand fluctuations.
- **Automotive marketplaces** monitor listing quality, completeness, and dealer behavior to improve platform reliability.
- **Researchers** gather structured datasets for modeling depreciation, availability, and consumer preference.
- **Developers** integrate real-time vehicle data into apps, price engines, or dashboards.

---

## FAQs

**Q: Can it extract full details from a single listing URL?**
Yes — simply paste the listing URL, and the scraper returns its full structured data.

**Q: How many results can be extracted per search?**
Up to 2000 results per search query. Larger datasets can be collected by splitting searches using exclusive search terms.

**Q: Does it collect dealer reviews and ratings?**
Yes — it extracts review text, scores, response times, languages, recommendation rate, and more.

**Q: What formats can the data be exported in?**
JSON, CSV, Excel, and several other structured formats.

---

## Performance Benchmarks and Results

**Primary Metric:** Extracts approximately **4 listings per second**, enabling fast collection of large datasets.
**Reliability Metric:** Maintains a high **success rate**, even across diverse search queries and listing types.
**Efficiency Metric:** Optimized parsing ensures **low resource usage** with consistent throughput across long runs.
**Quality Metric:** Produces **high-completeness structured data**, including detailed attributes, dealer metrics, image sets, and price ratings.


<p align="center">
<a href="https://calendar.app.google/74kEaAQ5LWbM8CQNA" target="_blank">
  <img src="https://img.shields.io/badge/Book%20a%20Call%20with%20Us-34A853?style=for-the-badge&logo=googlecalendar&logoColor=white" alt="Book a Call">
</a>
  <a href="https://www.youtube.com/@bitbash-demos/videos" target="_blank">
    <img src="https://img.shields.io/badge/🎥%20Watch%20demos%20-FF0000?style=for-the-badge&logo=youtube&logoColor=white" alt="Watch on YouTube">
  </a>
</p>
<table>
  <tr>
    <td align="center" width="33%" style="padding:10px;">
      <a href="https://youtu.be/MLkvGB8ZZIk" target="_blank">
        <img src="https://github.com/za2122/footer-section/blob/main/media/review1.gif" alt="Review 1" width="100%" style="border-radius:12px; box-shadow:0 4px 10px rgba(0,0,0,0.1);">
      </a>
      <p style="font-size:14px; line-height:1.5; color:#444; margin:0 15px;">
        “Bitbash is a top-tier automation partner, innovative, reliable, and dedicated to delivering real results every time.”
      </p>
      <p style="margin:10px 0 0; font-weight:600;">Nathan Pennington
        <br><span style="color:#888;">Marketer</span>
        <br><span style="color:#f5a623;">★★★★★</span>
      </p>
    </td>
    <td align="center" width="33%" style="padding:10px;">
      <a href="https://youtu.be/8-tw8Omw9qk" target="_blank">
        <img src="https://github.com/za2122/footer-section/blob/main/media/review2.gif" alt="Review 2" width="100%" style="border-radius:12px; box-shadow:0 4px 10px rgba(0,0,0,0.1);">
      </a>
      <p style="font-size:14px; line-height:1.5; color:#444; margin:0 15px;">
        “Bitbash delivers outstanding quality, speed, and professionalism, truly a team you can rely on.”
      </p>
      <p style="margin:10px 0 0; font-weight:600;">Eliza
        <br><span style="color:#888;">SEO Affiliate Expert</span>
        <br><span style="color:#f5a623;">★★★★★</span>
      </p>
    </td>
    <td align="center" width="33%" style="padding:10px;">
      <a href="https://youtube.com/shorts/6AwB5omXrIM" target="_blank">
        <img src="https://github.com/za2122/footer-section/blob/main/media/review3.gif" alt="Review 3" width="35%" style="border-radius:12px; box-shadow:0 4px 10px rgba(0,0,0,0.1);">
      </a>
      <p style="font-size:14px; line-height:1.5; color:#444; margin:0 15px;">
        “Exceptional results, clear communication, and flawless delivery. Bitbash nailed it.”
      </p>
      <p style="margin:10px 0 0; font-weight:600;">Syed
        <br><span style="color:#888;">Digital Strategist</span>
        <br><span style="color:#f5a623;">★★★★★</span>
      </p>
    </td>
  </tr>
</table>

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os

driver = webdriver.Chrome()

# Make sure 'data' folder exists
if not os.path.exists("data"):
    os.makedirs("data")

for i in range(1, 6):  # Scrape first 5 pages
    print(f"\nScraping Page {i}")
    driver.get(f"https://www.alibaba.com/trade/search?fsb=y&IndexArea=product_en&keywords=laptop&page={i}")
    
    try:
        elems = WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((
                By.CSS_SELECTOR,
                ".fy23-search-card.m-gallery-product-item-v2.J-search-card-wrapper.fy23-gallery-card.searchx-offer-item"
            ))
        )
    except:
        print("⚠️ No product cards found.")
        elems = []

    print(f"{len(elems)} product cards found.")

    # Save all HTMLs in one file per page
    with open(f"data/page_{i}.html", "w", encoding="utf-8") as f:
        for index, elem in enumerate(elems, start=1):
            card_html = elem.get_attribute("outerHTML")
            f.write(f"\n<!-- Product Card {index} -->\n")
            f.write(card_html + "\n")
            f.write("\n<!-- ---------------------------------- -->\n")

    time.sleep(2)  # delay to avoid bot detection

driver.quit()
print("\n✅ Done scraping full HTML of all cards.")

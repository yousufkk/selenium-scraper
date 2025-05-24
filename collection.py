from bs4 import BeautifulSoup
import csv
import os

data = []

# Loop through all HTML pages
for i in range(1, 6):  # page_1 to page_5
    file_path = f"data/page_{i}.html"
    if not os.path.exists(file_path):
        continue

    with open(file_path, "r", encoding="utf-8") as f:
        soup = BeautifulSoup(f, "html.parser")
        product_cards = soup.select(".search-card-info__wrapper")

        for card in product_cards:
            try:
                title = card.select_one(".search-card-e-title span").get_text(strip=True)
            except:
                title = ""

            try:
                price = card.select_one(".search-card-e-price-main").get_text(strip=True)
            except:
                price = ""

            try:
                company = card.select_one(".search-card-e-company").get_text(strip=True)
            except:
                company = ""

            try:
                link = card.select_one(".search-card-e-title a")["href"]
                if not link.startswith("http"):
                    link = "https:" + link
            except:
                link = ""

            data.append([title, price, company, link])

# Save to CSV
with open("product_data.csv", "w", newline="", encoding="utf-8") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["Title", "Price", "Company", "Link"])
    writer.writerows(data)

print("✅ CSV Export Done: product_data.csv")
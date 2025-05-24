from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
query = "Laptop"
for i in range(1,20):
    driver.get(f"https://www.alibaba.com/trade/search?fsb=y&IndexArea=product_en&keywords=laptop&originKeywords=laptop&tab=all&&page={i}&spm=a2700.galleryofferlist.pagination.0")

    try:
        elems = WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((
                By.CSS_SELECTOR,
                ".fy23-search-card.m-gallery-product-item-v2.J-search-card-wrapper.fy23-gallery-card.searchx-offer-item"
            ))
        )
    except:
        elems = []

    print(f"{len(elems)} product cards found:")
    for elem in elems:
        print("-" * 40)
        print(elem.text)

    driver.quit()
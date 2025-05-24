from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
query = "Laptop"
driver.get(f"https://www.alibaba.com/trade/search?spm=a2700.7735675.the-new-header_fy23_pc_search_bar.keydown__Enter&tab=all&SearchText={query}")
elem = driver.find_element(By.CSS_SELECTOR, ".fy23-search-card.m-gallery-product-item-v2.J-search-card-wrapper.fy23-gallery-card.searchx-offer-item")
print(elem.get_attribute("outerHTML"))
time.sleep(2)

driver.close()

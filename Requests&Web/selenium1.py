"""
selenium1.py
"""

import time
from bs4 import BeautifulSoup
from selenium import webdriver


driver = webdriver.Safari()


driver.get('https://www.imdb.com/title/tt0133093/')


time.sleep(1)
for i in range(30):
    y = i * 100
    driver.execute_script(f"window.scrollTo(0, {y});")
    time.sleep(0.3)



html = driver.page_source
soup = BeautifulSoup(html, "html.parser")

print("done100")
git
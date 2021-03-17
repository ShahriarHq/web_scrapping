# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("https://www.techwithtim.net")
print(driver.title)

search = driver.find_element_by_name("s")  # navigating the github search bar
search.send_keys("django")  # what we gonna search in the search bar
search.send_keys(Keys.RETURN)  # preesing the enger button with RETURN

try:
    with open("output.txt", "w") as output_file:
        main = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "main"))
        )
        articles = main.find_elements_by_tag_name("article")
        for article in articles:
            header = article.find_element_by_class_name("entry-summary")
            print(header.text)
            header1 = article.find_element_by_class_name("entry-meta")
            print(header1.text)
            output_file.write(header1.text)

            output_file.write(header.text)
finally:
    driver.quit()

driver.quit()

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

ser = Service("/Users/homefolder/chromedriver")
options = webdriver.ChromeOptions()
cookies = () # here are the cookies
entry_number = 250 #number of entries in the journal

driver = webdriver.Chrome(options=options)

out = open('output.txt', 'w')
next_url = 'https://posyo.livejournal.com/'
driver.get(next_url)
for ck in cookies:
    driver.add_cookie(ck)

driver.refresh()

header = driver.find_element(By.CLASS_NAME, 'entryunit__title')
header_link = header.find_elements(By.TAG_NAME, 'a')
header_link = [x.get_attribute('href') for x in header_link]
driver_get(header_link[0])

title = driver.find_element(By.CLASS_NAME, 'entry-title')
entry = driver.find_element(By.CLASS_NAME, 'entry-content')
date = driver.find_element(By.CLASS_NAME, 'dt-published')
year = date.find_elements(By.TAG_NAME, 'a')

out.write(year[0].text)
out.write(year[1].text)
out.write(year[2].text)
out.write('\n')
out.write(title.text)
out.write('\n')
out.write(entry.text)
out.write('\n\n')

record_counter = 0

try:
    while record_counter < entry_number:
        prev = driver.find_element(By.CLASS_NAME, 'b-singlepost-standout')
        prev_link = prev.find_elements(By.TAG_NAME, 'a')
        prev_link = [x.get_attribute('href') for x in prev_link]
        driver.get(prev_link[0])
        title = driver.find_element(By.CLASS_NAME, 'entry-title')
        entry = driver.find_element(By.CLASS_NAME, 'entry-content')
        date = driver.find_element(By.CLASS_NAME, 'dt-published')
        year = date.find_elements(By.TAG_NAME, 'a')
        out.write(year[0].text)
        out.write(year[1].text)
        out.write(year[2].text)
        out.write('\n')
        out.write(title.text)
        out.write('\n')
        out.write(entry.text)
        out.write('\n\n')

        record_counter += 1

finally:
    print(record_counter)
    driver.close()
    out.close()

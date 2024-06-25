import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd

chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=chrome_options)


url = "https://www.linkedin.com/pulse/topics/home/?trk=guest_homepage-basic_guest_nav_menu_articles"
driver.get(url)

time.sleep(5)
soup = BeautifulSoup(driver.page_source, 'lxml')
topics = []
topic_desc = []
datas = soup.find_all('h2', {'class': 'mb-1 overflow-hidden break-words font-sans text-lg font-[500] babybear:text-md'})
desc = soup.find_all('p',{'class':'content-description mt-0.5 break-words font-sans text-sm font-normal babybear:text-xs'})
for data in datas:
    topics.append(data.text)
    print(data.text)
print('--------------------------------------------------------------------------------------------------------------------')
for description in desc:
    topic_desc.append(description.text)
    print(description.text)
df = pd.DataFrame({'TOPIC':topics , 'DESC':topic_desc , })
driver.quit()
df.to_csv('topics.csv', index=False)

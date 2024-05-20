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


url = "https://github.com/aaronjoju07?tab=repositories"
driver.get(url)

time.sleep(5)


soup = BeautifulSoup(driver.page_source, 'lxml')

datas = soup.find_all('h3', {'class': 'wb-break-all'})

urls = []
texts = []
about =[]
fork=[]
star =[]
used_by=[]


for data in datas:
    a_tag = data.find('a') 
    if a_tag:
        repUrl = 'https://github.com/'+a_tag['href']
        urls.append(repUrl)  
        driver.get(repUrl)
        time.sleep(5)
        soup = BeautifulSoup(driver.page_source, 'lxml')
        descriptionDiv = soup.find('div', {'class': 'hide-sm hide-md'})
        if descriptionDiv:
            description_p = descriptionDiv.find('p')
            if description_p:
                description = description_p.text.strip()
                about.append(description)
            else:
                about.append("No description available")
        else:
            about.append("No description available")

        forkSpan = soup.find('span', {'id': 'repo-network-counter'}).text.strip()
        fork.append(forkSpan)
        starSpan = soup.find('span', {'id': 'repo-stars-counter-star'}).text.strip()
        star.append(starSpan)
        # usedBySpan = soup.find('span', {'id': 'repo-network-counter'}).text.strip()
        repName = a_tag.text
        texts.append(repName.strip()) 

df = pd.DataFrame({'URL': urls, 'Text': texts, 'About': about,'fork':fork,'star':star})
driver.quit()
df.to_csv('github.csv', index=False)
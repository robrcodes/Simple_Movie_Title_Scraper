from bs4 import BeautifulSoup as bs
import requests
import lxml
import random
import time

# website to be scraped
root = 'https://www.scripts.com'
website = f'{root}/scripts/A'  # movies starting with A

result = requests.get(website)
content = result.text
# parse the html
soup = bs(content, 'lxml')

# Pagination
#
pagination = soup.find('div', class_='pager')
pages = pagination.find_all('a', class_='rc5')

# pages[-2]  # last useful element that we need
last_page = pages[-2].text
print(f'Total pages to scrape: {last_page}')

# example of page url
# page 2 url = https://www.scripts.com/scripts/A/2

movie_list = []  # list to hold movie titles once scraped

for page in range(1, int(last_page)+1):  # 1 to last page
    titles_website = f'{website}/{page}'
    result = requests.get(titles_website)
    content = result.text
    soup = bs(content, 'lxml')

    # box for content of on page <table> element
    box_table = soup.find('table', class_='tdata')

    # all title text inside <strong> tags
    titles = box_table.find_all('strong')

    # feedback while running to display progress
    print(f'Scraping page number: {page}')

    # time delay between page requests in seconds
    page_delay = random.randint(1, 3)
    time.sleep(page_delay)


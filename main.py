from bs4 import BeautifulSoup as bs
import requests
import lxml

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
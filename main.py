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


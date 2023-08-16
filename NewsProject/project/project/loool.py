
import requests
import scrapy
from bs4 import BeautifulSoup

url = 'https://www.cybersport.ru/?sort=-publishedAt'
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

# news_titles = soup.find_all('h3', class_='title_nSS03')
# news_images = soup.select('.image_f4Qfq img[src]')
news_list = []
for article in soup.find_all('div', class_='rounded-block root_d51Rr with-hover no-padding no-margin'):
    title = article.find('h3', class_='title_nSS03').text.strip()
    link = article.find('a', class_='link_CocWY')['href']

    image_element = article.find('div', class_='image_f4Qfq')
    if image_element:
        image = image_element.find('img')['src']
    else:
        image = ""
    news_list.append({'title': title, 'link': link, 'image': image})

print(news_list)
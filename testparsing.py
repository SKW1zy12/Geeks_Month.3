from bs4 import BeautifulSoup
import requests


def klava():
    n = 0
    for page in range (1, 7):
        url = f'https://www.sulpak.kz/f/klaviaturiy/page={page}'
        response = (requests.get(url=url))
        soup = BeautifulSoup(response.text, 'lxml')
        klava_price = soup.find_all('div', class_='product__item-name')
        klava_name = soup.find_all('div', class_='product__item-price')
    
        for in zip(all_laptops, all_prices):
            n += 1
            print(n, laptop.text, "".join(price.text.split()))
klava()
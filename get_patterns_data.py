import requests
import shutil
from bs4 import BeautifulSoup
import csv
from itertools import islice
import random
import re

patterns_data = []

def get_soup(url):
    try:
        req = requests.get(url)
        soup = BeautifulSoup(req.text, "html.parser")
        return soup
    except Exception as e:
        return None
    
def get_number(s):
    match = re.search(r'№(\d+)', s)
    if match:
        return match.group(1)
    else:
        return random.randint(0, 2000 - 1)
    
def download_patterns(url, category, difficulty, season, style, volume, limit):
    soup = get_soup(url)
    cards = soup.find_all('div', {'class' : 'catalog-block'})
    # cards = soup.find_all('a', {'class' : 'woocommerce-LoopProduct-link woocommerce-loop-product__link'})4
    for i, card in enumerate(cards):
        a_title = card.find('a', {'class': 'catalog-block__title'})
        title = a_title.text.strip()
        id = get_number(title)
        price = card.find('div', {'class': 'catalog-block__price'}).text.replace('Р', '').strip().replace('Бесплатно', '0 0')
        patterns_data.append({'id': id, 'title': title, 'source': 'https://grasser.ru' + a_title['href'], 'price': price.split()[1], 'category': category,
                              'difficulty' : difficulty, 'season': season, 'style': style, 'volume': volume})
        if i == limit - 1: break


if __name__ == "__main__":
    #dresses
    download_patterns('https://grasser.ru/vykrojki/platya/?vikroyki_P1_MIN=&vikroyki_P1_MAX=&vikroyki_373_3193399236=Y&vikroyki_341_2362199700=Y&vikroyki_340_2077826809=Y&vikroyki_480_3220318196=Y&set_filter=submit',
                      category = 'dresses', difficulty = 1, season = 'summer', style = 'casual', volume = 1, limit = 4)
    download_patterns('https://grasser.ru/vykrojki/platya/?vikroyki_P1_MIN=&vikroyki_P1_MAX=&vikroyki_373_3193399236=Y&vikroyki_341_2362199700=Y&vikroyki_340_2077826809=Y&vikroyki_480_3371505506=Y&set_filter=submit',
                      category = 'dresses', difficulty = 1, season = 'summer', style = 'casual', volume = 2, limit = 5)
    download_patterns('https://grasser.ru/vykrojki/platya/?vikroyki_P1_MIN=&vikroyki_P1_MAX=&vikroyki_373_3193399236=Y&vikroyki_341_2362199700=Y&vikroyki_340_2077826809=Y&vikroyki_480_1481247475=Y&set_filter=submit',
                      category = 'dresses', difficulty = 1, season = 'summer', style = 'casual', volume = 3, limit = 6)
    download_patterns('https://grasser.ru/vykrojki/platya/?vikroyki_P1_MIN=&vikroyki_P1_MAX=&vikroyki_373_3193399236=Y&vikroyki_341_2362199700=Y&vikroyki_340_2623615998=Y&vikroyki_480_3220318196=Y&set_filter=submit'
                      , category = 'dresses', difficulty = 1, season = 'summer', style = 'evening', volume = 1, limit = 3)
    download_patterns('https://grasser.ru/vykrojki/platya/?vikroyki_P1_MIN=&vikroyki_P1_MAX=&vikroyki_373_3193399236=Y&vikroyki_341_2362199700=Y&vikroyki_340_2623615998=Y&vikroyki_480_3371505506=Y&set_filter=submit'
                      , category = 'dresses', difficulty = 1, season = 'summer', style = 'evening', volume = 2, limit = 2)
    download_patterns('https://grasser.ru/vykrojki/platya/?vikroyki_P1_MIN=&vikroyki_P1_MAX=&vikroyki_341_2362199700=Y&vikroyki_340_3949331304=Y&vikroyki_480_3220318196=Y&set_filter=submit'
                      , category = 'dresses', difficulty = 1, season = 'summer', style = 'classic', volume = 1, limit = 7)
    download_patterns('https://grasser.ru/vykrojki/platya/?vikroyki_P1_MIN=&vikroyki_P1_MAX=&vikroyki_341_2362199700=Y&vikroyki_340_3949331304=Y&vikroyki_480_3371505506=Y&set_filter=submit'
                      , category = 'dresses', difficulty = 1, season = 'summer', style = 'calssic', volume = 2, limit = 2)
    download_patterns('https://grasser.ru/vykrojki/platya/?vikroyki_P1_MIN=&vikroyki_P1_MAX=&vikroyki_341_2362199700=Y&vikroyki_340_3949331304=Y&vikroyki_480_1481247475=Y&set_filter=submit'
                      , category = 'dresses', difficulty = 1, season = 'summer', style = 'classic', volume = 3, limit = 4)
    

    download_patterns('https://grasser.ru/vykrojki/platya/?vikroyki_P1_MIN=&vikroyki_P1_MAX=&vikroyki_373_660485758=Y&vikroyki_341_2362199700=Y&vikroyki_340_2077826809=Y&vikroyki_480_3220318196=Y&set_filter=submit'
                      , category = 'dresses', difficulty = 2, season = 'summer', style = 'casual', volume = 1, limit = 30)
    download_patterns('https://grasser.ru/vykrojki/platya/?vikroyki_P1_MIN=&vikroyki_P1_MAX=&vikroyki_373_660485758=Y&vikroyki_341_2362199700=Y&vikroyki_340_2077826809=Y&vikroyki_480_3371505506=Y&set_filter=submit'
                      , category = 'dresses', difficulty = 2, season = 'summer', style = 'casual', volume = 2, limit = 21)
    download_patterns('https://grasser.ru/vykrojki/platya/?vikroyki_P1_MIN=&vikroyki_P1_MAX=&vikroyki_373_660485758=Y&vikroyki_341_2362199700=Y&vikroyki_340_2077826809=Y&vikroyki_480_1481247475=Y&set_filter=submit'
                      , category = 'dresses', difficulty = 2, season = 'summer', style = 'casual', volume = 3, limit = 12)
    download_patterns('https://grasser.ru/vykrojki/platya/?vikroyki_P1_MIN=&vikroyki_P1_MAX=&vikroyki_373_660485758=Y&vikroyki_341_2362199700=Y&vikroyki_340_2623615998=Y&vikroyki_480_3220318196=Y&set_filter=submit'
                      , category = 'dresses', difficulty = 2, season = 'summer', style = 'evening', volume = 1, limit = 21)
    download_patterns('https://grasser.ru/vykrojki/platya/?vikroyki_P1_MIN=&vikroyki_P1_MAX=&vikroyki_373_660485758=Y&vikroyki_341_2362199700=Y&vikroyki_340_2623615998=Y&vikroyki_480_3371505506=Y&set_filter=submit'
                      , category = 'dresses', difficulty = 2, season = 'summer', style = 'evening', volume = 2, limit = 5)
    download_patterns('https://grasser.ru/vykrojki/platya/?vikroyki_P1_MIN=&vikroyki_P1_MAX=&vikroyki_373_660485758=Y&vikroyki_341_2362199700=Y&vikroyki_340_2623615998=Y&vikroyki_480_1481247475=Y&set_filter=submit'
                      , category = 'dresses', difficulty = 2, season = 'summer', style = 'evening', volume = 3, limit = 3)
    download_patterns('https://grasser.ru/vykrojki/platya/?vikroyki_P1_MIN=&vikroyki_P1_MAX=&vikroyki_373_660485758=Y&vikroyki_341_2362199700=Y&vikroyki_340_3949331304=Y&vikroyki_480_3220318196=Y&set_filter=submit'
                      , category = 'dresses', difficulty = 2, season = 'summer', style = 'classic', volume = 1, limit = 3)
    download_patterns('https://grasser.ru/vykrojki/platya/?vikroyki_P1_MIN=&vikroyki_P1_MAX=&vikroyki_373_660485758=Y&vikroyki_341_2362199700=Y&vikroyki_340_3949331304=Y&vikroyki_480_3371505506=Y&set_filter=submit'
                      , category = 'dresses', difficulty = 2, season = 'summer', style = 'classic', volume = 2, limit = 2)
    download_patterns('https://grasser.ru/vykrojki/platya/?vikroyki_P1_MIN=&vikroyki_P1_MAX=&vikroyki_373_660485758=Y&vikroyki_341_2362199700=Y&vikroyki_340_3949331304=Y&vikroyki_480_1481247475=Y&set_filter=submit'
                      , category = 'dresses', difficulty = 2, season = 'summer', style = 'classic', volume = 3, limit = 1)
    
    download_patterns('https://grasser.ru/vykrojki/platya/?vikroyki_P1_MIN=&vikroyki_P1_MAX=&vikroyki_373_1348011752=Y&vikroyki_341_2362199700=Y&vikroyki_340_2077826809=Y&vikroyki_480_3220318196=Y&set_filter=submit'
                      , category = 'dresses', difficulty = 3, season = 'summer', style = 'casual', volume = 1, limit = 14)
    download_patterns('https://grasser.ru/vykrojki/platya/?vikroyki_P1_MIN=&vikroyki_P1_MAX=&vikroyki_373_1348011752=Y&vikroyki_341_2362199700=Y&vikroyki_340_2077826809=Y&vikroyki_480_3371505506=Y&set_filter=submit'
                      , category = 'dresses', difficulty = 3, season = 'summer', style = 'casual', volume = 2, limit = 13)
    download_patterns('https://grasser.ru/vykrojki/platya/?vikroyki_P1_MIN=&vikroyki_P1_MAX=&vikroyki_373_1348011752=Y&vikroyki_341_2362199700=Y&vikroyki_340_2077826809=Y&vikroyki_480_1481247475=Y&set_filter=submit'
                      , category = 'dresses', difficulty = 3, season = 'summer', style = 'casual', volume = 3, limit = 6)
    download_patterns('https://grasser.ru/vykrojki/platya/?vikroyki_P1_MIN=&vikroyki_P1_MAX=&vikroyki_373_1348011752=Y&vikroyki_341_2362199700=Y&vikroyki_340_2623615998=Y&vikroyki_480_3220318196=Y&set_filter=submit'
                      , category = 'dresses', difficulty = 3, season = 'summer', style = 'evening', volume = 1, limit = 12)
    download_patterns('https://grasser.ru/vykrojki/platya/?vikroyki_P1_MIN=&vikroyki_P1_MAX=&vikroyki_373_1348011752=Y&vikroyki_341_2362199700=Y&vikroyki_340_2623615998=Y&vikroyki_480_3371505506=Y&set_filter=submit'
                      , category = 'dresses', difficulty = 3, season = 'summer', style = 'evening', volume = 2, limit = 7)
    download_patterns('https://grasser.ru/vykrojki/platya/?vikroyki_P1_MIN=&vikroyki_P1_MAX=&vikroyki_373_1348011752=Y&vikroyki_341_2362199700=Y&vikroyki_340_3949331304=Y&vikroyki_480_3220318196=Y&set_filter=submit'
                      , category = 'dresses', difficulty = 3, season = 'summer', style = 'classic', volume = 1, limit = 3)
    
    download_patterns('https://grasser.ru/vykrojki/platya/?vikroyki_P1_MIN=&vikroyki_P1_MAX=&vikroyki_373_3193399236=Y&vikroyki_341_365240110=Y&set_filter=submit'
                      , category = 'dresses', difficulty = 0, season = 'winter', style = 'none', volume = 0, limit = 2)
    
    #blouses
    download_patterns('https://grasser.ru/vykrojki/bluzki-i-rubashki/?vikroyki_P1_MIN=&vikroyki_P1_MAX=&vikroyki_373_3193399236=Y&vikroyki_340_2077826809=Y&vikroyki_480_3371505506=Y&set_filter=submit'
                      ,category = 'blouses', difficulty = 1, season = 'none', style = 'casual', volume = 2, limit = 5)
    download_patterns('https://grasser.ru/vykrojki/bluzki-i-rubashki/?vikroyki_P1_MIN=&vikroyki_P1_MAX=&vikroyki_373_3193399236=Y&vikroyki_340_2077826809=Y&vikroyki_480_1481247475=Y&set_filter=submit'
                      ,category = 'blouses', difficulty = 1, season = 'none', style = 'casual', volume = 3, limit = 3)
    download_patterns('https://grasser.ru/vykrojki/bluzki-i-rubashki/?vikroyki_P1_MIN=&vikroyki_P1_MAX=&vikroyki_373_3193399236=Y&vikroyki_340_2623615998=Y&vikroyki_480_3220318196=Y&set_filter=submit'
                      ,category = 'blouses', difficulty = 1, season = 'none', style = 'evening', volume = 1, limit = 1)
    download_patterns('https://grasser.ru/vykrojki/bluzki-i-rubashki/?vikroyki_P1_MIN=&vikroyki_P1_MAX=&vikroyki_373_3193399236=Y&vikroyki_340_2623615998=Y&vikroyki_480_3371505506=Y&set_filter=submit'
                      ,category = 'blouses', difficulty = 1, season = 'none', style = 'evening', volume = 2, limit = 1)
    download_patterns('https://grasser.ru/vykrojki/bluzki-i-rubashki/?vikroyki_P1_MIN=&vikroyki_P1_MAX=&vikroyki_373_3193399236=Y&vikroyki_340_2623615998=Y&vikroyki_480_1481247475=Y&set_filter=submit'
                      ,category = 'blouses', difficulty = 1, season = 'none', style = 'evening', volume = 2, limit = 2)
    download_patterns('https://grasser.ru/vykrojki/bluzki-i-rubashki/?vikroyki_P1_MIN=&vikroyki_P1_MAX=&vikroyki_373_3193399236=Y&vikroyki_340_3949331304=Y&vikroyki_480_3220318196=Y&set_filter=submit'
                      ,category = 'blouses', difficulty = 1, season = 'none', style = 'classic', volume = 1, limit = 1)
    download_patterns('https://grasser.ru/vykrojki/bluzki-i-rubashki/?vikroyki_P1_MIN=&vikroyki_P1_MAX=&vikroyki_373_3193399236=Y&vikroyki_340_3949331304=Y&vikroyki_480_3371505506=Y&set_filter=submit'
                      ,category = 'blouses', difficulty = 1, season = 'none', style = 'classic', volume = 2, limit = 2)
    download_patterns('https://grasser.ru/vykrojki/bluzki-i-rubashki/?vikroyki_P1_MIN=&vikroyki_P1_MAX=&vikroyki_373_3193399236=Y&vikroyki_340_3949331304=Y&vikroyki_480_1481247475=Y&set_filter=submit'
                      ,category = 'blouses', difficulty = 1, season = 'none', style = 'classic', volume = 3, limit = 1)
    
    download_patterns('https://grasser.ru/vykrojki/bluzki-i-rubashki/?vikroyki_P1_MIN=&vikroyki_P1_MAX=&vikroyki_373_660485758=Y&vikroyki_340_2077826809=Y&vikroyki_480_3220318196=Y&set_filter=submit'
                      ,category = 'blouses', difficulty = 2, season = 'none', style = 'casual', volume = 1, limit = 7)
    download_patterns('https://grasser.ru/vykrojki/bluzki-i-rubashki/?vikroyki_P1_MIN=&vikroyki_P1_MAX=&vikroyki_373_660485758=Y&vikroyki_340_2077826809=Y&vikroyki_480_3371505506=Y&set_filter=submit'
                      ,category = 'blouses', difficulty = 2, season = 'none', style = 'casual', volume = 2, limit = 15)
    download_patterns('https://grasser.ru/vykrojki/bluzki-i-rubashki/?vikroyki_P1_MIN=&vikroyki_P1_MAX=&vikroyki_373_660485758=Y&vikroyki_340_2077826809=Y&vikroyki_480_1481247475=Y&set_filter=submit'
                      ,category = 'blouses', difficulty = 2, season = 'none', style = 'casual', volume = 3, limit = 12)
    download_patterns('https://grasser.ru/vykrojki/bluzki-i-rubashki/?vikroyki_P1_MIN=&vikroyki_P1_MAX=&vikroyki_373_660485758=Y&vikroyki_340_2623615998=Y&vikroyki_480_3220318196=Y&set_filter=submit'
                      ,category = 'blouses', difficulty = 2, season = 'none', style = 'evening', volume = 1, limit = 2)
    download_patterns('https://grasser.ru/vykrojki/bluzki-i-rubashki/?vikroyki_P1_MIN=&vikroyki_P1_MAX=&vikroyki_373_660485758=Y&vikroyki_340_2623615998=Y&vikroyki_480_3371505506=Y&set_filter=submit'
                      ,category = 'blouses', difficulty = 2, season = 'none', style = 'evening', volume = 2, limit = 6)
    download_patterns('https://grasser.ru/vykrojki/bluzki-i-rubashki/?vikroyki_P1_MIN=&vikroyki_P1_MAX=&vikroyki_373_660485758=Y&vikroyki_340_2623615998=Y&vikroyki_480_1481247475=Y&set_filter=submit'
                      ,category = 'blouses', difficulty = 2, season = 'none', style = 'evening', volume = 3, limit = 3)
    download_patterns('https://grasser.ru/vykrojki/bluzki-i-rubashki/?vikroyki_P1_MIN=&vikroyki_P1_MAX=&vikroyki_373_660485758=Y&vikroyki_340_3949331304=Y&vikroyki_480_3220318196=Y&set_filter=submit'
                      ,category = 'blouses', difficulty = 2, season = 'none', style = 'classic', volume = 1, limit = 6)
    download_patterns('https://grasser.ru/vykrojki/bluzki-i-rubashki/?vikroyki_P1_MIN=&vikroyki_P1_MAX=&vikroyki_373_660485758=Y&vikroyki_340_3949331304=Y&vikroyki_480_3371505506=Y&set_filter=submit'
                      ,category = 'blouses', difficulty = 2, season = 'none', style = 'classic', volume = 2, limit = 12)
    download_patterns('https://grasser.ru/vykrojki/bluzki-i-rubashki/?vikroyki_P1_MIN=&vikroyki_P1_MAX=&vikroyki_373_660485758=Y&vikroyki_340_3949331304=Y&vikroyki_480_1481247475=Y&set_filter=submit'
                      ,category = 'blouses', difficulty = 2, season = 'none', style = 'classic', volume = 3, limit = 3)
    
    download_patterns('https://grasser.ru/vykrojki/bluzki-i-rubashki/?vikroyki_P1_MIN=&vikroyki_P1_MAX=&vikroyki_373_1348011752=Y&vikroyki_340_2077826809=Y&vikroyki_480_3220318196=Y&set_filter=submit'
                      ,category = 'blouses', difficulty = 3, season = 'none', style = 'casual', volume = 1, limit = 4)
    download_patterns('https://grasser.ru/vykrojki/bluzki-i-rubashki/?vikroyki_P1_MIN=&vikroyki_P1_MAX=&vikroyki_373_1348011752=Y&vikroyki_340_2077826809=Y&vikroyki_480_3371505506=Y&set_filter=submit'
                       ,category = 'blouses', difficulty = 3, season = 'none', style = 'casual', volume = 2, limit = 12)
    download_patterns('https://grasser.ru/vykrojki/bluzki-i-rubashki/?vikroyki_P1_MIN=&vikroyki_P1_MAX=&vikroyki_373_1348011752=Y&vikroyki_340_2077826809=Y&vikroyki_480_1481247475=Y&set_filter=submit'
                      ,category = 'blouses', difficulty = 3, season = 'none', style = 'casual', volume = 3, limit = 13)
    download_patterns('https://grasser.ru/vykrojki/bluzki-i-rubashki/?vikroyki_P1_MIN=&vikroyki_P1_MAX=&vikroyki_373_1348011752=Y&vikroyki_340_2623615998=Y&vikroyki_480_3220318196=Y&set_filter=submit'
                      ,category = 'blouses', difficulty = 3, season = 'none', style = 'evening', volume = 1, limit = 3)
    download_patterns('https://grasser.ru/vykrojki/bluzki-i-rubashki/?vikroyki_P1_MIN=&vikroyki_P1_MAX=&vikroyki_373_1348011752=Y&vikroyki_340_2623615998=Y&vikroyki_480_3371505506=Y&set_filter=submit'
                      ,category = 'blouses', difficulty = 3, season = 'none', style = 'evening', volume = 2, limit = 5)
    download_patterns('https://grasser.ru/vykrojki/bluzki-i-rubashki/?vikroyki_P1_MIN=&vikroyki_P1_MAX=&vikroyki_373_1348011752=Y&vikroyki_340_2623615998=Y&vikroyki_480_1481247475=Y&set_filter=submit'
                      ,category = 'blouses', difficulty = 3, season = 'none', style = 'evening', volume = 3, limit = 4)
    download_patterns('https://grasser.ru/vykrojki/bluzki-i-rubashki/?vikroyki_P1_MIN=&vikroyki_P1_MAX=&vikroyki_373_1348011752=Y&vikroyki_340_3949331304=Y&vikroyki_480_3220318196=Y&set_filter=submit'
                      ,category = 'blouses', difficulty = 3, season = 'none', style = 'classic', volume = 1, limit = 3)
    download_patterns('https://grasser.ru/vykrojki/bluzki-i-rubashki/?vikroyki_P1_MIN=&vikroyki_P1_MAX=&vikroyki_373_1348011752=Y&vikroyki_340_3949331304=Y&vikroyki_480_3371505506=Y&set_filter=submit'
                      ,category = 'blouses', difficulty = 3, season = 'none', style = 'classic', volume = 2, limit = 6)
    download_patterns('https://grasser.ru/vykrojki/bluzki-i-rubashki/?vikroyki_P1_MIN=&vikroyki_P1_MAX=&vikroyki_373_1348011752=Y&vikroyki_340_3949331304=Y&vikroyki_480_1481247475=Y&set_filter=submit'
                      ,category = 'blouses', difficulty = 3, season = 'none', style = 'classic', volume = 3, limit = 3)
    
    #skirts
    download_patterns('https://grasser.ru/vykrojki/yubki/?vikroyki_P1_MIN=&vikroyki_P1_MAX=&vikroyki_341_365240110=Y&vikroyki_341_4224417282=Y&set_filter=submit'
                       ,category = 'skirts', difficulty = 0, season = 'winter', style = 'none', volume = 0, limit = 12)
    
    download_patterns('https://grasser.ru/vykrojki/yubki/?vikroyki_P1_MIN=&vikroyki_P1_MAX=&vikroyki_373_3193399236=Y&vikroyki_341_2362199700=Y&vikroyki_340_2077826809=Y&vikroyki_480_3220318196=Y&set_filter=submit'
                       ,category = 'skirts', difficulty = 1, season = 'summer', style = 'casual', volume = 1, limit = 5)
    download_patterns('https://grasser.ru/vykrojki/yubki/?vikroyki_P1_MIN=&vikroyki_P1_MAX=&vikroyki_373_3193399236=Y&vikroyki_341_2362199700=Y&vikroyki_340_2077826809=Y&vikroyki_480_3371505506=Y&set_filter=submit'
                       ,category = 'skirts', difficulty = 1, season = 'summer', style = 'casual', volume = 2, limit = 5)
    download_patterns('https://grasser.ru/vykrojki/yubki/?vikroyki_P1_MIN=&vikroyki_P1_MAX=&vikroyki_373_3193399236=Y&vikroyki_341_2362199700=Y&vikroyki_340_2077826809=Y&vikroyki_480_1481247475=Y&set_filter=submit'
                       ,category = 'skirts', difficulty = 1, season = 'summer', style = 'casual', volume = 3, limit = 5)
    download_patterns('https://grasser.ru/vykrojki/yubki/?vikroyki_P1_MIN=&vikroyki_P1_MAX=&vikroyki_341_2362199700=Y&vikroyki_340_2623615998=Y&vikroyki_480_3371505506=Y&set_filter=submit'
                       ,category = 'skirts', difficulty = 1, season = 'summer', style = 'evening', volume = 2, limit = 1)
    download_patterns('https://grasser.ru/vykrojki/yubki/?vikroyki_P1_MIN=&vikroyki_P1_MAX=&vikroyki_341_2362199700=Y&vikroyki_340_2623615998=Y&vikroyki_480_1481247475=Y&set_filter=submit'
                       ,category = 'skirts', difficulty = 1, season = 'summer', style = 'evening', volume = 3, limit = 2)
    download_patterns('https://grasser.ru/vykrojki/yubki/?vikroyki_P1_MIN=&vikroyki_P1_MAX=&vikroyki_341_2362199700=Y&vikroyki_340_3949331304=Y&vikroyki_480_3220318196=Y&set_filter=submit'
                       ,category = 'skirts', difficulty = 1, season = 'summer', style = 'classic', volume = 1, limit = 8)
    download_patterns('https://grasser.ru/vykrojki/yubki/?vikroyki_P1_MIN=&vikroyki_P1_MAX=&vikroyki_341_2362199700=Y&vikroyki_340_3949331304=Y&vikroyki_480_3371505506=Y&set_filter=submit'
                       ,category = 'skirts', difficulty = 1, season = 'summer', style = 'classic', volume = 2, limit = 5)
    download_patterns('https://grasser.ru/vykrojki/yubki/?vikroyki_P1_MIN=&vikroyki_P1_MAX=&vikroyki_341_2362199700=Y&vikroyki_340_3949331304=Y&vikroyki_480_1481247475=Y&set_filter=submit'
                       ,category = 'skirts', difficulty = 1, season = 'summer', style = 'classic', volume = 3, limit = 2)
    
    
    download_patterns('https://grasser.ru/vykrojki/yubki/?vikroyki_P1_MIN=&vikroyki_P1_MAX=&vikroyki_373_660485758=Y&vikroyki_341_2362199700=Y&vikroyki_340_2077826809=Y&vikroyki_480_3220318196=Y&set_filter=submit'
                      ,category = 'skirts', difficulty = 2, season = 'summer', style = 'casual', volume = 1, limit = 7)
    download_patterns('https://grasser.ru/vykrojki/yubki/?vikroyki_P1_MIN=&vikroyki_P1_MAX=&vikroyki_373_660485758=Y&vikroyki_341_2362199700=Y&vikroyki_340_2077826809=Y&vikroyki_480_3371505506=Y&set_filter=submit'
                      ,category = 'skirts', difficulty = 2, season = 'summer', style = 'casual', volume = 2, limit = 11)
    download_patterns('https://grasser.ru/vykrojki/yubki/?vikroyki_P1_MIN=&vikroyki_P1_MAX=&vikroyki_373_660485758=Y&vikroyki_341_2362199700=Y&vikroyki_340_2077826809=Y&vikroyki_480_1481247475=Y&set_filter=submit' 
                      ,category = 'skirts', difficulty = 2, season = 'summer', style = 'casual', volume = 3, limit = 1)
    download_patterns('https://grasser.ru/vykrojki/yubki/?vikroyki_P1_MIN=&vikroyki_P1_MAX=&vikroyki_373_660485758=Y&vikroyki_341_2362199700=Y&vikroyki_340_3949331304=Y&vikroyki_480_3220318196=Y&set_filter=submit'
                      ,category = 'skirts', difficulty = 2, season = 'summer', style = 'classic', volume = 1, limit = 4)
    download_patterns('https://grasser.ru/vykrojki/yubki/?vikroyki_P1_MIN=&vikroyki_P1_MAX=&vikroyki_373_660485758=Y&vikroyki_341_2362199700=Y&vikroyki_340_3949331304=Y&vikroyki_480_3371505506=Y&set_filter=submit'
                      ,category = 'skirts', difficulty = 2, season = 'summer', style = 'classic', volume = 2, limit = 3)

    
    download_patterns('https://grasser.ru/vykrojki/yubki/?vikroyki_P1_MIN=&vikroyki_P1_MAX=&vikroyki_373_1348011752=Y&vikroyki_341_2362199700=Y&vikroyki_340_2077826809=Y&set_filter=submit'
                      ,category = 'skirts', difficulty = 3, season = 'summer', style = 'casual', volume = 0, limit = 2)
    
    with open('data_patterns.csv', 'w', newline='') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=patterns_data[0].keys())
        writer.writeheader()
        writer.writerows(patterns_data)
    
    
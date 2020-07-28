import requests
from bs4 import BeautifulSoup
import re


def get_dd373():
    headers = {'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'}
    url = 'https://www.dd373.com/s-eja7u2-0r2mut-4vskce-kaebv3-0-0-jk5sj0-0-0-0-0-0-1-0-5-0.html'
    res = requests.get(url=url, headers=headers)
    contents = BeautifulSoup(res.text, 'html.parser')
    total_price = contents.find('div', class_='goods-list-item').find('div',class_='goods-price')
    re_total_price = re.findall('[1-9]\d*.\d*|0.\d*[1-9]\d*', total_price.text)
    per_price = contents.find('div', class_='goods-list-item').find('p', class_="font12 color666 m-t5")
    re_per_price = re.findall('[1-9]\d*.\d*|0.\d*[1-9]\d*', per_price.text)
    total_g = float(re_total_price[0])/float(re_per_price[1])
    print('DD373当前最低单价为%.4f,总量为%d'%((float(re_per_price[1])), int(total_g)))


if __name__ == '__main__':
    get_dd373()
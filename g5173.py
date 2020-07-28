import requests
from bs4 import BeautifulSoup
import re

def get_5173():
    headers = {'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'}
    url = 'http://s.5173.com/search/858f058e63e74156a1d4dcf3239df20c-ahp3ma-205jbk-4h3o3e-bwzkou-wr1n3g-0-0-0-a-a-a-a-a-0-0-0-0.shtml'
    res = requests.get(url=url, headers=headers)
    contents = BeautifulSoup(res.text, 'html.parser')
    total_price = contents.find('li', class_='pr')
    price = contents.find('ul', class_="pdlist_unitprice")
    per_price = re.findall('0.\d*[1-9]\d*', price.text)
    total_g = float(total_price.text)/float(per_price[0])
    print('5173当前最低单价为%.4f,总量为%d'%((float(per_price[0])), int(total_g)))

if __name__ == '__main__':
    get_5173()
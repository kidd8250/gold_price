import requests
from bs4 import BeautifulSoup
import re

def get_7881():
    headers = {'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'}
    url = 'https://search.7881.com/list.html?pageNum=1&gameId=G5569&gtid=100001&carrierId=0&groupId=G5569P002&serverId=G5569P002028&mobileGameType=&faceId=&tradeType=&tradePlace=&shopSortTypeCode=1&sortType=default&listSearchKeyWord=&mainSearchKeyWord=&minPrice=&maxPrice=&otherFilterValue=313346%3D%E8%81%94%E7%9B%9F&rentalByHourStart=&rentalByHourEnd=&propertiess=&chiledPropertiess=&platformId=&platformName=&order=&loginMethod=&rGameId=&tagName=&priceTag=&instock=false&quickChoose=0'
    res = requests.get(url=url, headers=headers)
    contents = BeautifulSoup(res.text, 'html.parser')
    total_price = contents.find('div', class_="list-item").find('div',class_="list-v part-02")
    re_total_price = re.findall('[1-9]\d*.\d*|0.\d*[1-9]\d*', total_price.text)
    per_price = contents.find('div', class_="list-item").find('div',class_="list-v part-03").find('p').find('em')
    total_g = float(re_total_price[0])/float(per_price.text)
    print('7881当前最低单价为%.4f,总量为%d'%((float(per_price.text)), int(total_g)))

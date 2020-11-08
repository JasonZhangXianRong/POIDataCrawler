import scrapy
from bs4 import BeautifulSoup
from POIDataCrawler.items import PoidatacrawlerItem
class PoilistSpider(scrapy.Spider):
    name = 'poilist'
    allowed_domains = ['poilist.cn']
    start_urls = ['http://www.poilist.cn/cities-list/%E7%BE%8E%E9%A3%9F']
    def parse(self, response):
        html_doc = response.body
        soup = BeautifulSoup(html_doc, 'lxml')
        for ulObj in soup.findAll("ul", {"class":"city-list"}):
            for liObj in ulObj.findAll("li"):
                href = "http://www.poilist.cn" + liObj.find("a").attrs["href"]
                for x in range(0, 34):
                    url = href +"/"+ str(30 * x)
                    yield scrapy.Request(url, self.getItem)
    def getItem(self, response):
        html_doc = response.body
        soup = BeautifulSoup(html_doc, 'lxml')
        for liObj in soup.find("div", {"class": "data-wrap"}).find("tbody").findAll("tr"):
            td = liObj.findAll("td")
            item = PoidatacrawlerItem()
            item['name'] = td[1].get_text()
            item['province'] = td[2].get_text()
            item['city'] = td[3].get_text()
            item['county'] = td[4].get_text()
            item['address'] = td[8].get_text()
            item['class1'] = td[9].get_text()
            item['class2'] = td[10].get_text()
            item['longitude'] = td[11].get_text()
            item['latitude'] = td[12].get_text()
            yield item









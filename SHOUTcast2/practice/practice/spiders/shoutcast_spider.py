import scrapy
import json
import requests

class SHOUTcastSpider(scrapy.Spider):
	name = "SHOUTcast"
	allowed_domains = ["http://shoutcast.com/"]
	start_urls = ["http://shoutcast.com/"]

	def parse(self,response):
		rq = requests.get("http://shoutcast.com/")
		header = {
			"Host": "shoutcast.com",
			"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.11; rv:43.0) Gecko/20100101 Firefox/43.0",
			"Accept": "*/*",
			"Accept-Language": "en-US,en;q=0.5",
			"Accept-Encoding": "gzip, deflate",
			"Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
			"X-Requested-With": "XMLHttpRequest",
			"Referer": "http://shoutcast.com/",
			"Content-Length": "27",
			"Cookie": "rq.cookies",
			"Connection": "keep-alive"
			}

		allgenre = response.selector.xpath('//a[contains(@id, "genre")]/text()').extract()

		with open("test.txt","w") as f:
			for i in range(len(allgenre)):
				f.write(allgenre[i]+'\n')
				formatdata = {"genrename":allgenre[i]}
				rq = requests.post('http://shoutcast.com/Home/BrowseByGenre', headers=header, data=formatdata)
				jsoncontent = json.loads(rq.content)
				print "Hello"
				for j in range(len(jsoncontent)):
					f.write('****Stations' + jsoncontent[j]['Name'])
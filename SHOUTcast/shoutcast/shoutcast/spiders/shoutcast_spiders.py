import scrapy

class SHOUTcastSpider(scrapy.Spider):
	name = "SHOUTcast"
	allowed_domains = ['http://shoutcast.com/']
	start_urls = ['http://shoutcast.com/']

	def parse(self, response):
		allmaingenre = response.selector.xpath('//option/text()').extract()
		allgenre = response.selector.xpath('//a[contains(@id, "genre")]/text()').extract()
		allgenrelink = response.selector.xpath('//a[contains(@id, "genre")]/@href').extract()

		with open('allgenre.txt','w') as f:
			for i in range(len(allgenre)):
				if allgenre[i] in allmaingenre:
					if i>0:
						f.write('\n' + allgenre[i]+'\n')
						f.write('Link:' + allgenrelink[i]+'\n')
					else:
						f.write(allgenre[i]+'\n')
						f.write('Link:' + allgenrelink[i]+'\n')
				else:
					f.write('***' + allgenre[i] + '\n')
					f.write('Link:' + allgenrelink[i]+'\n')

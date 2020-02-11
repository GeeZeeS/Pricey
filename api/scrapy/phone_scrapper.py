from scrapy import Spider, Request
# from api.models import (
#     Item, ItemBrand, ItemModel,
#     PhoneBody, PhoneCamera, PhoneDisplaySpec,
#     PhoneExtras, PhoneFeature, PhonesTechnicalSpec
# )


class PhoneInfoSpider(Spider):
    BASE_URL = 'https://www.scrooge.co.uk'
    name = 'phone_info_spider'
    start_urls = ['https://www.scrooge.co.uk/c/165/mobile_phones.html?order_by=pricevat&order_dir=desc&page=1']

    def parse(self, response):
        data = response.xpath('//*[@id="sku-list"]')
        for tab in data:
            urls = tab.xpath('//li/div[2]/h2/a/@href').extract()
            for url in urls:
                absolute_url = self.BASE_URL + url
                yield Request(absolute_url, callback=self.parse_details)

    def parse_details(self, response):
        item_model_raw = response.xpath('//*[@id="sku-info"]/div[1]/h1/text()').extract_first().strip()

        print(item_model_raw)

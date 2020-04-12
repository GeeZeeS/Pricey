from scrapy.spiders import CrawlSpider
from scrapy.http import Request
from api.models import Item, ItemCategory, ItemBrand, ItemModel


class PhoneInfoSpider(CrawlSpider):
    BASE_URL = 'https://www.scrooge.co.uk'
    CATEGORY_ID = 1
    PAGES_COUNT = 25
    # scrapy crawl phone_info_spider
    name = 'phone_info_spider'
    start_urls = [
        f'https://www.scrooge.co.uk/c/165/mobile_phones.html?order_by=pricevat&order_dir=desc&page={PAGES_COUNT}'
    ]

    def parse(self, response):
        for page in range(1, self.PAGES_COUNT):
            url = f'https://www.scrooge.co.uk/c/165/mobile_phones.html?order_by=pricevat&order_dir=desc&page={page}'
            yield Request(url, callback=self.parse_page)

    def parse_page(self, response):
        data = response.xpath('//*[@id="sku-list"]')
        for tab in data:
            urls = tab.xpath('//li/div[2]/h2/a/@href').extract()
            for url in urls:
                absolute_url = self.BASE_URL + url
                yield Request(absolute_url, callback=self.parse_details)

    def parse_details(self, response):
        item_category = ItemCategory.objects.get(pk=self.CATEGORY_ID)
        item_details_raw = response.xpath('//*[@id="sku-info"]/div[1]/h1/text()').extract_first().strip()

        item_brand_str = item_details_raw.split(' ')[0]
        item_brand, created = ItemBrand.objects.get_or_create(
            name=item_brand_str
        )

        item_model_str = item_details_raw.split(' ', 1)[1]
        head, sep, tail = item_model_str.partition('(')
        item_model, created = ItemModel.objects.get_or_create(
            brand=item_brand,
            name=head
        )

        item, created = Item.objects.get_or_create(
            model=item_model,
            category=item_category,
            name=item_model_str
        )
        print(item)
        yield None

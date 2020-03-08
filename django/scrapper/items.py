import scrapy
from scrapy_djangoitem import DjangoItem
from api.models import ItemBrand


class ItemBrandItem(DjangoItem):
    django_model = ItemBrand

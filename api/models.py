from django.db import models


###############################################################
# Item
###############################################################


class ItemCategory(models.Model):
    name = models.CharField(max_length=150)


class ItemBrand(models.Model):
    name = models.CharField(max_length=150)


class ItemModel(models.Model):
    brand = models.ForeignKey(ItemBrand, on_delete=models.CASCADE)
    name = models.CharField(max_length=150)


class Item(models.Model):
    name = models.CharField(max_length=255)
    model = models.ForeignKey(ItemModel, on_delete=models.CASCADE)
    category = models.ForeignKey(ItemCategory, on_delete=models.CASCADE)


###############################################################
# Phone Features
###############################################################

class PhonesTechnicalSpec(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    os = models.CharField(max_length=50)
    release_year = models.CharField(max_length=4)
    internal_memory = models.IntegerField()
    cpu_cores = models.CharField(max_length=20)
    cpu_speed = models.CharField(max_length=20)
    chipset = models.CharField(max_length=50)
    ram = models.IntegerField()
    card_slot = models.BooleanField()


class PhoneDisplaySpec(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    screen_size = models.CharField(max_length=5)
    screen_type = models.CharField(max_length=255)
    screen_resolution = models.CharField(max_length=50)


class PhoneFeature(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)

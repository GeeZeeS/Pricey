from django.db import models


###############################################################
# Item
###############################################################


class ItemCategory(models.Model):
    name = models.CharField(max_length=150)

    class Meta:
        verbose_name = 'Item Category'
        verbose_name_plural = 'Item Categories'


class ItemBrand(models.Model):
    name = models.CharField(max_length=150)

    class Meta:
        verbose_name = 'Item Brand'
        verbose_name_plural = 'Item Brands'


class ItemModel(models.Model):
    brand = models.ForeignKey(ItemBrand, on_delete=models.CASCADE)
    name = models.CharField(max_length=150)

    class Meta:
        verbose_name = 'Item Model'
        verbose_name_plural = 'Item Models'


class Item(models.Model):
    name = models.CharField(max_length=255)
    model = models.ForeignKey(ItemModel, on_delete=models.CASCADE)
    category = models.ForeignKey(ItemCategory, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Item'
        verbose_name_plural = 'Items'


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

    class Meta:
        verbose_name = 'Phone Technical Spec'
        verbose_name_plural = 'Phone Technical Specs'


class PhoneFeature(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    sim = models.CharField(max_length=10)
    connectivity = models.CharField(max_length=255)
    network = models.CharField(max_length=5)

    class Meta:
        verbose_name = 'Phone Feature'
        verbose_name_plural = 'Phone Features'


class PhoneDisplaySpec(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    screen_size = models.CharField(max_length=5)
    screen_type = models.CharField(max_length=255)
    screen_resolution = models.CharField(max_length=50)

    class Meta:
        verbose_name = 'Phone Display Spec'
        verbose_name_plural = 'Phone Display Specs'


class PhoneBody(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    dimensions = models.CharField(max_length=255)
    weight = models.CharField(max_length=10)

    class Meta:
        verbose_name = 'Phone Body'
        verbose_name_plural = 'Phone Bodies'


class PhoneCamera(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    primary_camera = models.CharField(max_length=10)
    rear_camera = models.CharField(max_length=10)
    front_camera = models.CharField(max_length=10)
    dual_front_camera = models.BooleanField(default=False)
    dual_rear_camera = models.BooleanField(default=False)
    triple_rear_camera = models.BooleanField(default=False)
    built_in_flash = models.BooleanField(default=False)
    front_flash = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Phone Camera'
        verbose_name_plural = 'Phone Cameras'


class PhoneExtras(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    resistance = models.CharField(max_length=255)
    sensors = models.CharField(max_length=255)
    fingerprint = models.BooleanField(default=False)
    ip_rating = models.CharField(max_length=52)

    class Meta:
        verbose_name = 'Phone Extra'
        verbose_name_plural = 'Phone Extras'





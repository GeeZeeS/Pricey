from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import AbstractBaseUser, AbstractUser, BaseUserManager
from django_resized import ResizedImageField
from django.conf import settings


####################################################################################################
# Account Structure
####################################################################################################

class UserManager(BaseUserManager):

    def create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError("Users must have an Email")

        if not email:
            raise ValueError('The Email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError("Users must have an Email")

        if not email:
            raise ValueError('The Email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        return self._create_user(email, password, **extra_fields)


class User(AbstractBaseUser):
    email = models.EmailField(verbose_name='email', unique=True, blank=True, null=True)
    username = models.CharField(max_length=30, unique=True, blank=True, null=True)
    first_name = models.CharField(max_length=50, unique=False, blank=True, null=True)
    last_name = models.CharField(max_length=50, unique=False, blank=True, null=True)
    image_url = ResizedImageField(
        size=[100, 100], crop=['middle', 'center'], quality=75, force_format='JPEG',
        blank=True, null=True, upload_to='user_images/%Y/%m/%d/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now_add=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'

    objects = UserManager()

    @classmethod
    def get_full_name(cls):
        return f'{cls.first_name} {cls.last_name}'

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True


####################################################################################################
# Mixins Model
####################################################################################################


class AbstractInfoModel(models.Model):
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL, null=True, on_delete=models.SET_NULL,
        verbose_name=_('Creator'), related_name='%(class)s_create_user')
    updated_by = models.ForeignKey(
        settings.AUTH_USER_MODEL, null=True, on_delete=models.SET_NULL,
        verbose_name=_('Editor'), related_name='%(class)s_update_user')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True


###############################################################
# Item
###############################################################


class ItemCategory(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Item Category'
        verbose_name_plural = 'Item Categories'
        ordering = ['name']


class ItemBrand(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Item Brand'
        verbose_name_plural = 'Item Brands'
        ordering = ['name']


class ItemModel(models.Model):
    brand = models.ForeignKey(ItemBrand, on_delete=models.CASCADE)
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Item Model'
        verbose_name_plural = 'Item Models'
        ordering = ['name']


class Item(models.Model):
    model = models.ForeignKey(ItemModel, on_delete=models.CASCADE)
    category = models.ForeignKey(ItemCategory, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Item'
        verbose_name_plural = 'Items'
        ordering = ['name']


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

    def __str__(self):
        return self.item.name

    class Meta:
        verbose_name = 'Phone Technical Spec'
        verbose_name_plural = 'Phone Technical Specs'


class PhoneFeature(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    sim = models.CharField(max_length=10)
    connectivity = models.CharField(max_length=255)
    network = models.CharField(max_length=5)

    def __str__(self):
        return self.item.name

    class Meta:
        verbose_name = 'Phone Feature'
        verbose_name_plural = 'Phone Features'


class PhoneDisplaySpec(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    screen_size = models.CharField(max_length=5)
    screen_type = models.CharField(max_length=255)
    screen_resolution = models.CharField(max_length=50)

    def __str__(self):
        return self.item.name

    class Meta:
        verbose_name = 'Phone Display Spec'
        verbose_name_plural = 'Phone Display Specs'


class PhoneBody(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    dimensions = models.CharField(max_length=255)
    weight = models.CharField(max_length=10)

    def __str__(self):
        return self.item.name

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

    def __str__(self):
        return self.item.name

    class Meta:
        verbose_name = 'Phone Camera'
        verbose_name_plural = 'Phone Cameras'


class PhoneExtras(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    resistance = models.CharField(max_length=255)
    sensors = models.CharField(max_length=255)
    fingerprint = models.BooleanField(default=False)
    ip_rating = models.CharField(max_length=52)

    def __str__(self):
        return self.item.name

    class Meta:
        verbose_name = 'Phone Extra'
        verbose_name_plural = 'Phone Extras'





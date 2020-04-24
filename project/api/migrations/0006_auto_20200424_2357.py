# Generated by Django 3.0.2 on 2020-04-24 20:57

from django.db import migrations, models
import django_resized.forms


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_item_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('email', models.EmailField(blank=True, max_length=254, null=True, unique=True, verbose_name='email')),
                ('username', models.CharField(blank=True, max_length=30, null=True, unique=True)),
                ('first_name', models.CharField(blank=True, max_length=50, null=True)),
                ('last_name', models.CharField(blank=True, max_length=50, null=True)),
                ('image_url', django_resized.forms.ResizedImageField(blank=True, crop=['middle', 'center'], force_format='JPEG', keep_meta=True, null=True, quality=75, size=[100, 100], upload_to='user_images/%Y/%m/%d/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('last_login', models.DateTimeField(auto_now_add=True)),
                ('is_admin', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_superuser', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AlterModelOptions(
            name='item',
            options={'ordering': ['name'], 'verbose_name': 'Item', 'verbose_name_plural': 'Items'},
        ),
        migrations.AlterModelOptions(
            name='itembrand',
            options={'ordering': ['name'], 'verbose_name': 'Item Brand', 'verbose_name_plural': 'Item Brands'},
        ),
        migrations.AlterModelOptions(
            name='itemcategory',
            options={'ordering': ['name'], 'verbose_name': 'Item Category', 'verbose_name_plural': 'Item Categories'},
        ),
        migrations.AlterModelOptions(
            name='itemmodel',
            options={'ordering': ['name'], 'verbose_name': 'Item Model', 'verbose_name_plural': 'Item Models'},
        ),
    ]

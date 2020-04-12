# Generated by Django 3.0.2 on 2020-02-10 20:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='ItemBrand',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='ItemCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='PhonesTechnicalSpec',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('os', models.CharField(max_length=50)),
                ('release_year', models.CharField(max_length=4)),
                ('internal_memory', models.IntegerField()),
                ('cpu_cores', models.CharField(max_length=20)),
                ('cpu_speed', models.CharField(max_length=20)),
                ('chipset', models.CharField(max_length=50)),
                ('ram', models.IntegerField()),
                ('card_slot', models.BooleanField()),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Item')),
            ],
        ),
        migrations.CreateModel(
            name='PhoneFeature',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sim', models.CharField(max_length=10)),
                ('connectivity', models.CharField(max_length=255)),
                ('network', models.CharField(max_length=5)),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Item')),
            ],
        ),
        migrations.CreateModel(
            name='PhoneDisplaySpec',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('screen_size', models.CharField(max_length=5)),
                ('screen_type', models.CharField(max_length=255)),
                ('screen_resolution', models.CharField(max_length=50)),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Item')),
            ],
        ),
        migrations.CreateModel(
            name='ItemModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.ItemBrand')),
            ],
        ),
        migrations.AddField(
            model_name='item',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.ItemCategory'),
        ),
        migrations.AddField(
            model_name='item',
            name='model',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.ItemModel'),
        ),
    ]
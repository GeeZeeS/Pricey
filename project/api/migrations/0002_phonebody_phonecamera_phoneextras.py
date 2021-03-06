# Generated by Django 3.0.2 on 2020-02-10 21:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PhoneExtras',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('resistance', models.CharField(max_length=255)),
                ('sensors', models.CharField(max_length=255)),
                ('fingerprint', models.BooleanField(default=False)),
                ('ip_rating', models.CharField(max_length=52)),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Item')),
            ],
        ),
        migrations.CreateModel(
            name='PhoneCamera',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('primary_camera', models.CharField(max_length=10)),
                ('rear_camera', models.CharField(max_length=10)),
                ('front_camera', models.CharField(max_length=10)),
                ('dual_front_camera', models.BooleanField(default=False)),
                ('dual_rear_camera', models.BooleanField(default=False)),
                ('triple_rear_camera', models.BooleanField(default=False)),
                ('built_in_flash', models.BooleanField(default=False)),
                ('front_flash', models.BooleanField(default=False)),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Item')),
            ],
        ),
        migrations.CreateModel(
            name='PhoneBody',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dimensions', models.CharField(max_length=255)),
                ('weight', models.CharField(max_length=10)),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Item')),
            ],
        ),
    ]

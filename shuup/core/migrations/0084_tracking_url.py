# Generated by Django 2.2.15 on 2021-02-26 18:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shuup', '0083_make_attribute_name_256_chars'),
    ]

    operations = [
        migrations.AddField(
            model_name='shipment',
            name='tracking_url',
            field=models.URLField(blank=True, verbose_name='tracking url'),
        ),
    ]
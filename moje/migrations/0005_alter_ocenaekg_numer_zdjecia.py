# Generated by Django 5.2.4 on 2025-07-14 22:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('moje', '0004_alter_ocenaekg_numer_zdjecia'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ocenaekg',
            name='numer_zdjecia',
            field=models.IntegerField(default=0),
        ),
    ]

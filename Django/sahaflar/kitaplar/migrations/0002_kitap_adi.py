# Generated by Django 3.1.1 on 2020-09-24 13:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kitaplar', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='kitap',
            name='adi',
            field=models.CharField(default='.', max_length=200),
            preserve_default=False,
        ),
    ]
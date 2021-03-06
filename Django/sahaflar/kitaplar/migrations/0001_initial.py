# Generated by Django 3.1.1 on 2020-09-24 08:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Yazar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('adi', models.CharField(max_length=200)),
                ('tc_kimlik_no', models.CharField(max_length=11)),
            ],
        ),
        migrations.CreateModel(
            name='Kitap',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('yili', models.DateField(auto_now=True)),
                ('notlar', models.TextField(blank=True, null=True)),
                ('yazar', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kitaplar.yazar')),
            ],
        ),
    ]

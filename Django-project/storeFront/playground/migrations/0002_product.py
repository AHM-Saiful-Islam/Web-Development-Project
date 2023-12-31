# Generated by Django 5.0 on 2023-12-13 00:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('playground', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=1000)),
                ('stock', models.IntegerField()),
                ('category', models.CharField(max_length=200)),
                ('price', models.FloatField()),
                ('company', models.CharField(max_length=500)),
            ],
        ),
    ]

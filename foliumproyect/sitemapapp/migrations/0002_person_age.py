# Generated by Django 4.0 on 2022-03-31 10:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sitemapapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='age',
            field=models.IntegerField(default=0),
        ),
    ]
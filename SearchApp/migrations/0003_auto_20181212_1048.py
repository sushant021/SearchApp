# Generated by Django 2.1.4 on 2018-12-12 05:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('SearchApp', '0002_auto_20181212_0012'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='author',
            options={'ordering': ('-name',)},
        ),
    ]

# Generated by Django 2.1.1 on 2018-09-27 19:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0002_auto_20180927_1943'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='pub_data',
            field=models.DateTimeField(),
        ),
    ]

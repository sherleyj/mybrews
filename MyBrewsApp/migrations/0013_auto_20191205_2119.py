# Generated by Django 2.2.7 on 2019-12-06 03:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MyBrewsApp', '0012_auto_20191205_2044'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='notes',
            field=models.TextField(blank=True, null=True),
        ),
    ]

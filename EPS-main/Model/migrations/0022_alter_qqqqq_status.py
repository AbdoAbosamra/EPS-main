# Generated by Django 3.2 on 2021-04-19 21:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Model', '0021_qqqqq'),
    ]

    operations = [
        migrations.AlterField(
            model_name='qqqqq',
            name='Status',
            field=models.CharField(max_length=200, null=True),
        ),
    ]

# Generated by Django 3.2 on 2021-04-19 21:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Model', '0017_auto_20210419_2103'),
    ]

    operations = [
        migrations.AlterField(
            model_name='questions',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]

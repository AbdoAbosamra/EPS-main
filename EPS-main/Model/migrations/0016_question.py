# Generated by Django 3.2 on 2021-04-19 21:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Model', '0015_auto_20210419_1948'),
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Bady', models.CharField(max_length=1000)),
                ('Correct_Answer', models.CharField(max_length=20)),
                ('User_Answer', models.CharField(max_length=20)),
                ('Status', models.CharField(choices=[('Indoor', 'Indoor'), ('Out Door', 'Out Door')], max_length=200, null=True)),
            ],
        ),
    ]
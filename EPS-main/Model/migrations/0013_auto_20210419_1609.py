# Generated by Django 3.2 on 2021-04-19 16:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Model', '0012_auto_20210419_1553'),
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('answer', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.AlterModelOptions(
            name='question',
            options={'ordering': ['question_name']},
        ),
        migrations.RemoveField(
            model_name='question',
            name='answer',
        ),
        migrations.RemoveField(
            model_name='question',
            name='body',
        ),
        migrations.AddField(
            model_name='question',
            name='question_image',
            field=models.ImageField(default=50, upload_to='levels/'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='question',
            name='question_name',
            field=models.CharField(default=' ', max_length=20, unique=True),
        ),
        migrations.AddField(
            model_name='question',
            name='question_text',
            field=models.TextField(blank=True, max_length=100),
        ),
        migrations.DeleteModel(
            name='Quiz',
        ),
        migrations.AddField(
            model_name='answer',
            name='question_relation',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Model.question'),
        ),
    ]

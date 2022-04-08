# Generated by Django 4.0.3 on 2022-04-08 08:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={},
        ),
        migrations.RemoveField(
            model_name='user',
            name='active',
        ),
        migrations.RemoveField(
            model_name='user',
            name='date_of_birth',
        ),
        migrations.RemoveField(
            model_name='user',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='user',
            name='last_name',
        ),
        migrations.AlterField(
            model_name='question',
            name='more_description',
            field=models.TextField(blank=True, null=True),
        ),
    ]

# Generated by Django 4.0.3 on 2022-04-08 08:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0002_alter_comment_options_remove_user_active_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='staffstatus',
            field=models.BooleanField(default=False),
        ),
    ]

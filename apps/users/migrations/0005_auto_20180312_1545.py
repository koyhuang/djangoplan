# Generated by Django 2.0.2 on 2018-03-12 07:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20180312_1536'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='EmailVerfyRecord',
            new_name='EmailVerifyRecord',
        ),
    ]

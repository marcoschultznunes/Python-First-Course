# Generated by Django 3.1.6 on 2021-02-11 23:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0005_auto_20210211_2257'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='posts',
            new_name='tags',
        ),
    ]

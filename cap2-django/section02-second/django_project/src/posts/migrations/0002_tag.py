# Generated by Django 3.1.6 on 2021-02-11 22:40

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40, validators=[django.core.validators.MinLengthValidator(2)])),
                ('posts', models.ManyToManyField(to='posts.Post', verbose_name='tags_posts')),
            ],
        ),
    ]
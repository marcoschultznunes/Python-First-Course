# Generated by Django 3.1.5 on 2021-01-26 04:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='user',
            table='users',
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('content', models.CharField(max_length=3000)),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.user')),
            ],
            options={
                'db_table': 'posts',
            },
        ),
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('login', models.CharField(max_length=100)),
                ('verified', models.BooleanField(default=False)),
                ('user_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='app.user')),
            ],
            options={
                'db_table': 'accounts',
            },
        ),
    ]
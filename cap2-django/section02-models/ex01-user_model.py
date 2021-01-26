"""
    To create a model in django we use a class extending models.Model, imported from django.db 
"""

# On models.py
from django.db import models

class User(models.Model):
    name = models.CharField(max_length = 150) # String
    email = models.CharField(max_length = 100)
    password = models.CharField(max_length = 40)

"""
    Then we make the migrations with the command
        python manage.py makemigrations
"""


# A file called 0001_initial.py will be created in the migrations folder
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('email', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=40)),
            ],
        ),
    ]


"""
    Then we can migrate with 
        python manage.py migrate
"""

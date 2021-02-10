"""
    We'll now add the created_at and updated_at timestamps to the user model
"""
from django.db import models

class User(models.Model):
    name = models.CharField(max_length = 150)
    email = models.CharField(max_length = 100)
    password = models.CharField(max_length = 40)


    # TIMESTAMPS
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.email

    class Meta:
        db_table = "users"


"""
    after that, run the migrations, select 1 to add a default value to the date field, then 
    set it to timezone.now()
"""

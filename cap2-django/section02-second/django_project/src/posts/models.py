from django.db import models
from django.core.validators import MinLengthValidator

class Post(models.Model):
    title = models.CharField(max_length=300, validators=[MinLengthValidator(2)])
    content = models.CharField(max_length=3000, validators=[MinLengthValidator(1)])

    class Meta:
        verbose_name_plural = 'Posts'

    def __str__(self):
        return self.title



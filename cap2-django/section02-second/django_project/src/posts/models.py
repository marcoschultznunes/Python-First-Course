from django.db import models
from django.core.validators import MinLengthValidator, FileExtensionValidator
from django.core.exceptions import ValidationError
from uuid import uuid4
import time;

# Validators

def image_size(image):
    limit = 10 * 1024 * 1024
    if image.size > limit:
        raise ValidationError('Image size should not exceed 10 MB.')

def upload_destination(instance, filename):
    ext = filename.split('.')[-1]
    name = filename.split('.')[0]
    ts = str(time.time()).replace('.', '')
    finalname = f"postImages/{name}_{uuid4()}_{ts}.{ext}"

    return finalname


# Models

class Tag(models.Model):
    name = models.CharField(max_length=40, validators=[MinLengthValidator(2)])

    def __str__(self):
        return self.name 

class Post(models.Model):
    title = models.CharField(max_length=300, validators=[MinLengthValidator(2)])
    content = models.CharField(max_length=3000, validators=[MinLengthValidator(1)])

    image = models.ImageField(
        upload_to = upload_destination, 
        null = True, 
        validators = [
            image_size,
            FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png'])
        ]
    )

    tags = models.ManyToManyField(
        "Tag", verbose_name=("posts_tags"), related_name='posts', blank=True
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Posts'

    def __str__(self):
        return self.title

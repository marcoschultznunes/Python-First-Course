"""
    In this example, we'll add some validators to our image field.

    - We'll add a limit of 10MB;
    - By default, django already restricts the extensions in an image field, but we'll still
    customize it. (FileExtensionValidator class of django core)

    NOTE: Why i decided not to validade max width and height:
        https://stackoverflow.com/questions/49214386/django-with-pil-io-bytesio-object-has-no-attribute-name
"""

from django.core.validators import MinLengthValidator, FileExtensionValidator
from django.core.exceptions import ValidationError

def image_size(image):
    limit = 10 * 1024 * 1024
    if image.size > limit:
        raise ValidationError('Image size should not exceed 10 MB.')


class Post(models.Model):

    image = models.ImageField(
        upload_to='postImages', null=True, validators=[
            image_size,
            FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png'])
        ]
    )

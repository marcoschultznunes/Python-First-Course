"""
    Now i'll add an image field to post, then add it to the serializers
"""

class Post(models.Model):
    title = models.CharField(max_length=300, validators=[MinLengthValidator(2)])
    content = models.CharField(max_length=3000, validators=[MinLengthValidator(1)])

    image = models.ImageField(upload_to='postImages', null=True)

    tags = models.ManyToManyField(
        "Tag", verbose_name=("posts_tags"), related_name='posts', blank=True
    )

    class Meta:
        verbose_name_plural = 'Posts'

    def __str__(self):
        return self.title

"""
    Then run
        python manage.py makemigrations
        python manage.py migrate

    And add the "image" field to the serializers.


    NOTE: Don't forget to turn off authentication is settings.py to test with insomnia.
    We'll need insomnia!
"""

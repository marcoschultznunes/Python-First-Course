"""
    https://stackoverflow.com/questions/42031864/django-absract-vs-non-abstract-model-inheritance
"""

class Annotation(models.Model):
    body = models.TextField()

    class Meta:
        abstract = True # Makes the model abstract


class BookAnnotation(Annotation):
    book = models.ForeignKey(Book, blank=True)

    class Meta:
        default_related_name = 'book_annotations'


class ArticleAnnotation(Annotation):
    article = models.ForeignKey(Article, blank=True)

    class Meta:
        default_related_name = 'article_annotations'

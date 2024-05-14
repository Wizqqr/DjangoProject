from django.db import models

class PostBooks(models.Model):
    name = models.CharField(max_length=100, verbose_name='Enter the name of the book', null=True)
    author = models.CharField(max_length=100, verbose_name='Name of author', null=True)
    publication_date = models.DateTimeField(auto_now_add=True, null=True)
    genre = models.CharField(max_length=100, verbose_name='Enter the genre of the book', null=True)
    language = models.CharField(max_length=100, verbose_name='Enter the language of the book', null=True)
    num_pages = models.IntegerField(null=True)
    video = models.URLField(verbose_name='Send a link', blank=True, null=True)
    description = models.CharField(max_length=100, verbose_name='Write some information', null=True)
    image = models.ImageField(upload_to='images/', verbose_name='Upload a picture please', blank=True, null=True)
    music = models.FileField(upload_to='audio/', verbose_name='Upload a music file', blank=True, null=True)
    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Books'
        verbose_name_plural = 'List of books'

class Review(models.Model):
    book = models.ForeignKey(PostBooks, related_name='reviews', on_delete=models.CASCADE)
    stars = models.IntegerField()
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Review for {self.book.name}'

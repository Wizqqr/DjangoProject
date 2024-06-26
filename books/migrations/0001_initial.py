# Generated by Django 5.0.4 on 2024-05-08 17:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PostNews',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Enter the name of the post')),
                ('image', models.ImageField(blank=True, upload_to='images/', verbose_name='Upload a picture please')),
                ('description', models.TextField(verbose_name='Write news')),
                ('music', models.FileField(blank=True, upload_to='audio/', verbose_name='Upload a music file')),
                ('video', models.URLField(verbose_name='Send a link')),
                ('category_news', models.CharField(choices=[('Sport', 'Sport'), ('Politics', 'Politics'), ('Science', 'Science'), ('Technology', 'Technology'), ('Entertainment', 'Entertainment'), ('Health', 'Health')], max_length=100, verbose_name='Choose a category')),
                ('time_news', models.PositiveIntegerField(verbose_name='Say the time of news')),
                ('author', models.CharField(max_length=100, null=True, verbose_name='Name of author')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'News',
                'verbose_name_plural': 'List of news',
            },
        ),
    ]

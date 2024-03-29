# Generated by Django 5.0.1 on 2024-01-17 06:20

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0004_categories_category_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='detailnews',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='news_categories', to='news.categories'),
        ),
        migrations.RemoveField(
            model_name='detailnews',
            name='tag_name',
        ),
        migrations.AddField(
            model_name='detailnews',
            name='tag_name',
            field=models.ManyToManyField(related_name='news_tags', to='news.tags'),
        ),
    ]

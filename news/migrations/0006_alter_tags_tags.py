# Generated by Django 5.0.1 on 2024-01-17 06:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0005_alter_detailnews_category_remove_detailnews_tag_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tags',
            name='tags',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]

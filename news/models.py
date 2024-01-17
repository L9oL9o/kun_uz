# from django.db.models import *
#
#
# class Categories(Model):
#     category_name = CharField(max_length=255)
#
#     def __str__(self):
#         return self.category_name
#
#
# class Tags(Model):
#     tags = CharField(max_length=100)
#
#     def save(self, *args, **kwargs):
#         # Проверяем, начинается ли строка с символа #
#         if not self.tags.startswith('#'):
#             # Если нет, добавляем символ #
#             self.tags = '#' + self.tags
#         # Вызываем оригинальный метод save
#         super().save(*args, **kwargs)
#
#     def __str__(self):
#         return self.tags
#
#
# class DetailNews(Model):
#     title = CharField(max_length=255)
#     detail_text = TextField()
#     img_url = URLField()
#     pub_date = DateTimeField(auto_now_add=True)
#     category = ForeignKey(Categories, on_delete=CASCADE)
#     tag_name = ForeignKey(Tags, on_delete=CASCADE)
#
#     def __str__(self):
#         return self.title
#
#
# class ShortNews(DetailNews):
#     pub_date = DateTimeField(auto_now_add=True)
#
#     def __str__(self):
#         return self.title
#
#     class Meta:
#         exclude = ['detail_text', 'tag_name', ]
#


# news/py
# from django.db import models
from django.db.models import *


class Categories(Model):
    category_number = IntegerField(null=True)
    category_name = CharField(max_length=255)

    def __str__(self):
        return self.category_name

    class Meta:
        verbose_name_plural = "Categories"

class Tags(Model):
    tags = CharField(max_length=100)

    def save(self, *args, **kwargs):
        if not self.tags.startswith('#'):
            self.tags = '#' + self.tags
        super().save(*args, **kwargs)

    def __str__(self):
        return self.tags

    class Meta:
        verbose_name_plural = 'Tags'


class DetailNews(Model):
    title = CharField(max_length=255)
    short_text = CharField(max_length=255)
    detail_text = TextField()
    img_url = URLField()
    pub_date = DateTimeField(auto_now_add=True)
    category = ForeignKey(Categories, on_delete=CASCADE)
    # category = ManyToManyField(Categories)
    tag_name = ForeignKey(Tags, on_delete=CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Detail News"


class ShortNews(DetailNews):

    def __str__(self):
        return self.title

    class Meta:
        proxy = True
        verbose_name_plural = "Short News"

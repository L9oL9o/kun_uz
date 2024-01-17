# from django.shortcuts import render
# from news.models import *
#
# def test_view(request):
#     # Your view logic here
#     return render(request, 'base.html')
#
#
# def Categories_view(request):
#     categories = Categories.objects.all()
#     context = {'category': categories}
#     return render(request, 'base.html', context)
#
#
# def Detail_news_view(request, news_id):
#     news_item = DetailNews.objects.get(id=news_id)
#     detail_news_list =
#     return render(request, 'base.html', {'news_item': news_item})
#
#
# def Short_news_view(request, category_id):
#     short_news_category = ShortNews.objects.get(id=category_id)
#     category_news_list = ShortNews.objects.filter(category_id=category_id)
#     return render(request, 'base.html', {'category_news_list': category_news_list})


# news/views.py
from django.shortcuts import render, get_object_or_404
from django.views import View
from .models import Categories, DetailNews, ShortNews


class CategoriesView(View):
    def get(self, request):
        categories = Categories.objects.all()
        context = {'category': categories}
        return render(request, 'categories.html', context)


class DetailNewsView(View):
    def get(self, request, news_id):
        detail_news_item = get_object_or_404(DetailNews, id=news_id)
        return render(request, 'detail_news.html', {'detail_new_item': detail_news_item})

    # def get(self, request, category_id, news_id):
    #     from_category = get_object_or_404(Categories, id=category_id)
    #     detail_news_item = get_object_or_404(DetailNews, id=news_id, category=from_category)
    #     return render(request, 'detail_news.html', {'detail_news_item': detail_news_item})


class ShortNewsView(View):

    def get(self, request, category_id, short_news_id):
        short_news_id = ShortNews.objects.get(id=short_news_id)
        short_news_list = ShortNews.objects.filter(category=category_id and short_news_id)
        return render(request, "short_news.html", {'short_news_list': short_news_list})


class ShortNewsDetailView(View):
    def get(self, request, category_id):
        category_id = Categories.objects.get(id=category_id)
        short_news = get_object_or_404(ShortNews, id=category_id)
        return render(request, "short_news.html", {'short_news_item': short_news})

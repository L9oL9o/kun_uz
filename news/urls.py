# from django.urls import path
#
# from news.views import test_view
#
# urlpatterns = [
#     path('', test_view)
# ]


# news/urls.py
from django.urls import path
from .views import CategoriesView, DetailNewsView, ShortNewsView, ShortNewsDetailView

urlpatterns = [
    # path('', views)
    path('categories/', CategoriesView.as_view(), name='categories'),
    path('detail-news/<int:news_id>/', DetailNewsView.as_view(), name='detail_news'),

    # path('detail-news/<int:category_id>/<int:news_id>/', DetailNewsView.as_view(), name='detail_news'),
    path('short/<int:category_id>/', ShortNewsView.as_view(), name='short_news'),
    path('short/detail/<int:news_id>/', ShortNewsDetailView.as_view(), name='short_news_detail'),
]

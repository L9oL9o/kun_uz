from django.urls import path

from news.views import test_view

urlpatterns = [
    path('', test_view)
]

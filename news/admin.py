from django.contrib import admin
from news.models import *

admin.site.register(Categories)

admin.site.register(DetailNews)
admin.site.register(ShortNews)
admin.site.register(Tags)

from django.contrib import admin

# Register your models here.

from .models import news,blog

admin.site.register(news)
admin.site.register(blog)

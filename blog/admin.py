# -*- coding: utf-8 -*-
from django.contrib import admin

from .models import Category, Post


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'slug')
    search_fields = ('name', 'slug')


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display_links = ('id', 'title', 'slug')
    list_display = ('id', 'title', 'slug', 'category',)
    list_filter = ('category',)
    search_fields = ('slug',)

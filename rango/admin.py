from django.contrib import admin
from django.contrib import admin
from rango.models import Category, Page
from django import forms

class PageAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'url')
admin.site.register(Category)
admin.site.register(Page,PageAdmin)
# Register your models here.

from django.contrib import admin
from .models import Photo, Category

# Register your models here.


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')


class PhotoAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'category', 'user')
    list_display_links = ('id', 'title', 'category')


admin.site.register(Category, CategoryAdmin)
admin.site.register(Photo, PhotoAdmin)

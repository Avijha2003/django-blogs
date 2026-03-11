from django.contrib import admin
from .models import Blog, category

class BlogAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_display = ("title", "status", "author", "category", "is_featured")
    search_fields = ("title", "id", "category__category_name","status")
    list_editable = ("status", "is_featured")

admin.site.register(category)
admin.site.register(Blog, BlogAdmin)
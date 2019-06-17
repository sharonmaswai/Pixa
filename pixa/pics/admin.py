from django.contrib import admin
from .models import Location, Image, Category

class ArticleAdmin(admin.ModelAdmin):
    filter_horizontal =('Category',)


admin.site.register(Image)
admin.site.register(Location)
admin.site.register(Category)


# Register your models here.

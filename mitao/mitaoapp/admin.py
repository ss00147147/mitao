from django.contrib import admin
from .models import news

# Register your models here.
class ColumnAdmin(admin.ModelAdmin):
    list_display = ('content',)

    

admin.site.register(news,ColumnAdmin)

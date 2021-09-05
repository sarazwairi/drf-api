from django.contrib import admin
from .models import Things
# Register your models here.
admin.site.register(Things)

# @admin.register(Things)
# class AuthorAdmin(admin.ModelAdmin):
#     list_display=('title','purchaser')
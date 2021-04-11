from django.contrib import admin
from .models import FAQ, Category, CategoryMap
# Register your models here.
admin.site.register(FAQ)
admin.site.register(Category)
admin.site.register(CategoryMap)
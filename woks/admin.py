from django.contrib import admin

from .models import Category
from .models import Series
from .models import Chapter


admin.site.register(Category)
admin.site.register(Series)
admin.site.register(Chapter)

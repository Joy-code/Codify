from django.contrib import admin
from .models import Category, Difficulty, codingQ, Attempt

# Register your models here.
admin.site.register(Category)
admin.site.register(Difficulty)
admin.site.register(codingQ)
admin.site.register(Attempt)
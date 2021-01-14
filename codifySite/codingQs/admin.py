from django.contrib import admin
from .models import Category, Difficulty, codingQ, Attempt

class codingQsInline(admin.TabularInline):
    model = codingQ

@admin.register(Category) 
class CategoryAdmin(admin.ModelAdmin):
    inlines = [codingQsInline]

@admin.register(Difficulty)
class DifficultyAdmin(admin.ModelAdmin): 
    inlines = [codingQsInline]



class AttemptsInline(admin.TabularInline):
    model = Attempt

@admin.register(codingQ) 
class codingQAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'difficulty', 'status')
    list_filter = ('category', 'difficulty', 'status')
    inlines = [AttemptsInline]

@admin.register(Attempt)
class AttemptAdmin(admin.ModelAdmin):
    pass

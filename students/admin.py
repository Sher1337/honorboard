from django.contrib import admin
from .models import Student, Nomination

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name')
    search_fields = ('first_name', 'last_name')
    list_filter = ('nominations',)

@admin.register(Nomination)
class NominationAdmin(admin.ModelAdmin):
    list_display = ('name',)

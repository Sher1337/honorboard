from django.contrib import admin
from .models import Student, Nomination

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'get_nominations')
    search_fields = ('first_name', 'last_name')
    list_filter = ('nominations',)

    def get_nominations(self, obj):
        return ", ".join([nomination.name for nomination in obj.nominations.all()])
    get_nominations.short_description = 'Nominations'


@admin.register(Nomination)
class NominationAdmin(admin.ModelAdmin):
    list_display = ('name',)

from django.contrib import admin
from list.models import Programme, inst, Category
# Register your models here.
class ProgrammeAdmin(admin.ModelAdmin):
	list_display = ('name', 'inst', 'code')
admin.site.register(Programme, ProgrammeAdmin)
# Register your models here.

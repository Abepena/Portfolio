from django.contrib import admin
from .models import Job, Project, Technology, Resume
# Register your models here.

class TechnologyInline(admin.TabularInline):
    model = Technology

class ProjectAdmin(admin.ModelAdmin):
    inlines = [TechnologyInline]

admin.site.register(Job)
admin.site.register(Resume)
admin.site.register(Project, ProjectAdmin)
admin.site.register(Technology)

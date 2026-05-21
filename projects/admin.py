from django.contrib import admin

from .models import Project, ProjectImage


class ProjectImageInline(admin.TabularInline):
    model = ProjectImage
    extra = 1


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ("title", "status", "category", "location", "order", "status_active")
    list_editable = ("status", "category", "order", "status_active")
    list_filter = ("status", "category", "status_active")
    search_fields = ("title", "description", "location")
    inlines = [ProjectImageInline]


@admin.register(ProjectImage)
class ProjectImageAdmin(admin.ModelAdmin):
    list_display = ("project", "caption", "uploaded_at")
    search_fields = ("project__title", "caption")

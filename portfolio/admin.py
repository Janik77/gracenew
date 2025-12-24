from django.contrib import admin

from .models import Project, ProjectImage


class ProjectImageInline(admin.TabularInline):
    model = ProjectImage
    extra = 1


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "category",
        "client",
        "city",
        "year",
        "is_featured",
        "created_at",
    )
    list_filter = ("category", "city", "year", "is_featured")
    search_fields = ("title", "client", "category", "city")
    prepopulated_fields = {"slug": ("title",)}
    inlines = [ProjectImageInline]

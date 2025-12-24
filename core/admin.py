from django.contrib import admin

from .models import LeadRequest, SiteSettings


@admin.register(SiteSettings)
class SiteSettingsAdmin(admin.ModelAdmin):
    list_display = ("phone", "email", "instagram_url")


@admin.register(LeadRequest)
class LeadRequestAdmin(admin.ModelAdmin):
    list_display = ("name", "phone", "page", "created_at")
    search_fields = ("name", "phone", "page")

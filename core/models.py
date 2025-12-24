from django.db import models


class SiteSettings(models.Model):
    phone = models.CharField(max_length=50, blank=True)
    whatsapp = models.CharField(max_length=50, blank=True)
    email = models.EmailField(blank=True)
    address = models.CharField(max_length=255, blank=True)
    working_hours = models.CharField(max_length=255, blank=True)
    instagram_url = models.URLField(blank=True)
    map_url = models.URLField(blank=True)
    hero_title = models.CharField(max_length=255, blank=True)
    hero_subtitle = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return "Site Settings"

    @classmethod
    def get_solo(cls):
        instance, _created = cls.objects.get_or_create(pk=1)
        return instance


class LeadRequest(models.Model):
    name = models.CharField(max_length=120)
    phone = models.CharField(max_length=50)
    message = models.TextField(blank=True)
    page = models.CharField(max_length=255, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.name} ({self.phone})"

from django.core.management.base import BaseCommand
from django.utils.text import slugify

from core.models import SiteSettings
from portfolio.models import Project, ProjectImage


class Command(BaseCommand):
    help = "Seed demo data for site settings and portfolio projects."

    def handle(self, *args, **options):
        SiteSettings.get_solo()
        categories = [
            "Объёмные буквы",
            "Фасады",
            "Стеллы",
            "Интерьер",
            "Печать",
            "Дизайн",
        ]
        created_projects = 0
        for index, category in enumerate(categories, start=1):
            title = f"Проект {index} — {category}"
            slug = slugify(title)
            project, created = Project.objects.get_or_create(
                slug=slug,
                defaults={
                    "title": title,
                    "short_description": f"{category}: заметное решение для бизнеса.",
                    "description": (
                        "Проект выполнен под ключ: от дизайн-концепции до монтажа. "
                        "Материалы подобраны с учётом условий эксплуатации."
                    ),
                    "category": category,
                    "client": f"Клиент {index}",
                    "city": "Москва",
                    "year": 2024,
                    "is_featured": index <= 3,
                    "cover_image": "projects/covers/placeholder.jpg",
                },
            )
            if created:
                created_projects += 1
                for image_index in range(1, 3):
                    ProjectImage.objects.create(
                        project=project,
                        image="projects/gallery/placeholder.jpg",
                        alt=f"{title} изображение {image_index}",
                        sort_order=image_index,
                    )
        self.stdout.write(
            self.style.SUCCESS(
                f"Seeded demo data. Projects created: {created_projects}."
            )
        )

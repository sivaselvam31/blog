from typing import Any
from blogapp.models import Post, category
from django.core.management.base import BaseCommand



class Command(BaseCommand):
    help = "This command inserts catergory data"


    def handle(self, *args: Any, **options: Any) -> str | None:
        # Delete existing data
        category.objects.all().delete()

        categories = ['Sports', 'Technology', 'Science', 'Art', 'Food']

        for category_name in categories:
            category.objects.create(name = category_name)
        
        self.stdout.write(self.style.SUCCESS("Completed inserting Data!"))
from django.core.management import BaseCommand

from news.models import NewPost


class Command(BaseCommand):
    help = "reset post upvotes count"

    def handle(self, *args, **options):
        post_list = NewPost.objects.all()
        for post in post_list:
            post.upvotes_amount = 0
            post.save()
            self.stdout.write(self.style.SUCCESS(f"Successfully {post.id}"))

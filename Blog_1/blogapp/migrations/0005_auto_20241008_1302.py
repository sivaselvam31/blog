from django.db import migrations
from django.utils.text import slugify

def generate_slugs(apps, schema_editor):
    Post = apps.get_model('blogapp', 'Post')
    for post in Post.objects.all():
        post.slug = slugify(post.title)
        post.save()

class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0004_post_slug'),
    ]

    operations = [
        migrations.RunPython(generate_slugs),
    ]

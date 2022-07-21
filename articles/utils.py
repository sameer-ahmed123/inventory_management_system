import random
from django.utils.text import slugify



def slugify_instance_title(instance, save=False, new_slug=None):
    if new_slug is not None:
        slug = new_slug
    else:
        slug = slugify(instance.title)
    klass = instance.__class__
    qs = klass.objects.filter(slug=slug).exclude(id=instance.id)
    if qs.exists():
        random_int = random.randint(300_000, 500_000 )
        slug = f"{slug}-{random_int}"
        return slugify_instance_title(instance, save=False,new_slug=slug)
    instance.slug = slug
    if save:
        instance.save()
    return instance

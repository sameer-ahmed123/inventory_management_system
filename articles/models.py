from django.db import models
from  django.db.models.signals import pre_save,post_save
from django.urls import reverse

from django.utils import timezone
from django.db.models import Q
# default=timezone.now() put this in datefield to auto add date to previous empty fields
from .utils import slugify_instance_title
# Create your models here.
class Article_queryset_manager(models.QuerySet):
    def search(self,query=None ):
        if query is  None or query == "":
            return self.none()
        lookups = Q(title__icontains=query ) | Q(content__icontains=query ) # | Q(published__contains=query )
        return self.filter(lookups)

class Article_Manager(models.Manager):
    def get_queryset(self):
        return Article_queryset_manager(self.model, using=self._db)

    def search(self,  query=None):
        return self.get_queryset().search(query=query)




class Article(models.Model):
    user = models.ForeignKey("auth.User", blank=True, null=True, on_delete=models.SET_NULL) #on_delete=models.CASCADE
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True,max_length=50 ,blank=True, null=True)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    published = models.DateField(auto_now_add=True, auto_now=False, null=True, blank=True)


    objects = Article_Manager()

    def get_absolute_url(self):
        # return f"/articles/{self.slug}/"
        return reverse("article-detail", kwargs={"slug":self.slug})

    class Meta:
        ordering = ['-timestamp']
        db_table = "article"

    # def save(self,*args, **kwargs):
    #     if self.slug is None:
    #         slugify_instance_title(self, save=False)
    #     super().save(*args,**kwargs)



def article_pre_save(sender , instance, *args, **kwargs):
    #print("pre_save")
    if instance.slug is None:
        slugify_instance_title(instance, save=False)


pre_save.connect(article_pre_save, sender=Article)


def article_post_save(sender, instance , created, *args, **kwargs):
    #print("post_save")
    if created:
        slugify_instance_title(instance, save=True)


post_save.connect(article_post_save, sender=Article)


import string

from django.db import models
from django.utils import timezone
from django.utils.text import slugify
from django.db.models.signals import post_save, pre_save

# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length=222, db_index=True)
    slug = models.SlugField(unique=True, null=True, blank=True)
    image = models.ImageField(upload_to='articles',null=True, blank=True, help_text='2MB dan oshmasin!')
    content = models.TextField()
    is_deleted = models.BooleanField(default=False)
    modified_date = models.DateTimeField(auto_now=True, null=True)
    created_date= models.DateTimeField(auto_now_add=True, null=True)


    def __str__(self):
        return f"{self.title} ({self.id})"
    # def save(self, force_insert=False, force_update=False, using=None, updated_fields=None):
    #     if self.slug is None:
    #         self.slug = slugify(self.title)
    #
    #     try:
    #      super().save()
    #     except Exception as e:
    #         rand = "".join(random.choise(string.ascii_lowercase) for _ in range(4))
    #         self.slug = slugify(self.title) + f"{rand}"
    #         super().save()

from django.db import models
from django.urls import reverse

class Blog(models.Model):
    title       = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    author     = models.CharField(max_length=200)
    featured    = models.BooleanField(default=False)  # null=True, default=True

    #blank: how the field is rendered
    #null: how the database handles the info

    def get_absolute_url(self):  #with app_name in urls.py
        return reverse("blog:blog_detail", kwargs={"id": self.id})
        

class Article(models.Model):
    title       = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    author     = models.CharField(max_length=200)
    featured    = models.BooleanField(default=False)  # null=True, default=True

    #blank: how the field is rendered
    #null: how the database handles the info

    def get_absolute_url(self):  #with app_name in urls.py
        return reverse("blog:article_detail", kwargs={"pk": self.pk})

    # success_url (in views.py) overwrites "get_absolute_url"
    # alt to "get_absolute_url":
        # def get_success_url(self)
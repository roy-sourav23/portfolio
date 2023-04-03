from django.db import models
from django.urls import reverse

# Create your models here.


class Project(models.Model):
    name = models.CharField(max_length=155)
    cover = models.ImageField(upload_to="covers/", blank=True)
    details = models.TextField(blank=True)
    codeLink = models.CharField(max_length=155, blank=True)
    demo = models.CharField(max_length=155, blank=True)

    def __str__(self):
        return self.name


class Message(models.Model):
    fname = models.CharField(max_length=120, verbose_name="First Name")
    lname = models.CharField(max_length=120, verbose_name="Last Name")
    email = models.EmailField(max_length=254)
    phone = models.TextField(max_length=10, verbose_name="Phone No.")
    message = models.TextField(blank=False)

    def __str__(self):
        return self.message

    def get_absolute_url(self):
        return reverse("contact")

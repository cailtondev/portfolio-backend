from django.contrib.auth.models import User  # noqa
from django.db import models


class Home(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title


class WebDevelopmentOffer(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    paragraph = models.CharField(max_length=255)

    def __str__(self):
        return self.title


class WebDevelopmentCard(models.Model):
    id = models.AutoField(primary_key=True)
    card_title = models.CharField(max_length=150)
    card_paragraph = models.CharField(max_length=100)


class WebDevelopmentTechnologies(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50)
    icon_link = models.TextField()

    def __str__(self):
        return self.title


class WebDevelopmentProjects(models.Model):
    id = models.AutoField(primary_key=True)
    tag = models.CharField(max_length=30, default='#Front-End')
    image_link = models.TextField()
    alt_image = models.CharField(max_length=100)
    link_preview = models.TextField()

    def __str__(self):
        return self.tag


class ResumeME(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=80)
    paragraph = models.TextField()

    def __str__(self):
        return self.title


class Contact(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=30)
    paragraph = models.CharField(max_length=200)
    email = models.CharField(max_length=250)
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=50)

    def __str__(self):
        return self.title

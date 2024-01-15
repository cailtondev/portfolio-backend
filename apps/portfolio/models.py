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
    offer = models.ForeignKey(WebDevelopmentOffer, on_delete=models.CASCADE)
    card_title = models.CharField(max_length=150)
    card_paragraph = models.CharField(max_length=100)

    def __str__(self):
        return self.card_title


class WebDevelopmentTechnologies(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50)
    icon_link = models.CharField(max_length=255)

    def __str__(self):
        return self.title


class WebDevelopmentProjects(models.Model):
    id = models.AutoField(primary_key=True)
    tag = models.CharField(max_length=30, default='#Front-End')
    title = models.CharField(max_length=255)
    paragraph = models.CharField(max_length=255)
    image_link = models.CharField(max_length=255)
    alt_image = models.CharField(max_length=100)
    link_preview = models.CharField(max_length=255)

    def __str__(self):
        return self.title


class ResumeME(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=80)
    paragraph = models.TextField()

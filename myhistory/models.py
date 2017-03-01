from django.db import models
from django.utils import timezone


class Profile(models.Model):
    name = models.CharField(max_length=200)
    mission_statement = models.TextField(blank=True, null=True)
    created_date = models.DateTimeField(default=timezone.now)
    birthday = models.DateTimeField(blank=True, null=True)
    dream1 = models.CharField(max_length=200, blank=True, null=True)
    dream2 = models.CharField(max_length=200, blank=True, null=True)
    dream3 = models.CharField(max_length=200, blank=True, null=True)
    stronPoint1 = models.CharField(max_length=200, blank=True, null=True)
    stronPoint2 = models.CharField(max_length=200, blank=True, null=True)
    stronPoint3 = models.CharField(max_length=200, blank=True, null=True)
    weekPoint1 = models.CharField(max_length=200, blank=True, null=True)
    weekPoint2 = models.CharField(max_length=200, blank=True, null=True)
    weekPoint3 = models.CharField(max_length=200, blank=True, null=True)
    profile_image = models.ImageField(upload_to='images/')

    def publish(self):
        self.save()

    def __str__(self):
        return self.title

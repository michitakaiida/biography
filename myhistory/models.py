from django.db import models
from django.utils import timezone


class Profile(models.Model):
    name = models.CharField(max_length=200)
    mission_statement = models.TextField(blank=True, null=True)
    created_date = models.DateTimeField(default=timezone.now)
    birthday = models.DateField(blank=True, null=True)
    dream1 = models.CharField(max_length=200, blank=True, null=True)
    dream2 = models.CharField(max_length=200, blank=True, null=True)
    dream3 = models.CharField(max_length=200, blank=True, null=True)
    strongPoint1 = models.CharField(max_length=200, blank=True, null=True)
    strongPoint2 = models.CharField(max_length=200, blank=True, null=True)
    strongPoint3 = models.CharField(max_length=200, blank=True, null=True)
    weekPoint1 = models.CharField(max_length=200, blank=True, null=True)
    weekPoint2 = models.CharField(max_length=200, blank=True, null=True)
    weekPoint3 = models.CharField(max_length=200, blank=True, null=True)
    profile_image = models.ImageField(upload_to='images/', null=True)

    def publish(self):
        self.save()

    def __str__(self):
        return self.name


class Timeline(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    timeline_name = models.CharField(max_length=200, blank=True, null=False)

    def __str__(self):
        return self.timeline_name


class Event(models.Model):
    event_size_choice = (
        (1, 1),
        (2, 2),
        (3, 3)
    )
    event_type_id = models.ForeignKey(Timeline, on_delete=models.CASCADE)
    event_name = models.CharField(max_length=30, blank=True, null=True)
    event_size = models.PositiveSmallIntegerField(choices=event_size_choice, null=False)
    event_date = models.DateField(null=False)
    turningpoint_flag = models.BooleanField()

    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.event_name

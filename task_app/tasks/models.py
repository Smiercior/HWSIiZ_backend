from django.db import models
from django.contrib.auth.models import User
# from Auth import User


class Ability(models.Model):
    SKILL_LEVEL_CHOICES = (
        ('beginner', 'beginner'),
        ('intermediate', 'intermediate'),
        ('advanced', 'advanced'),
        ('expert', 'expert'),
    )
    name = models.CharField(max_length=128)
    level = models.CharField(max_length=16, choices=SKILL_LEVEL_CHOICES)


class Project(models.Model):
    title = models.CharField(max_length=128)
    description = models.TextField()
    leader = models.ForeignKey(User, on_delete=models.CASCADE)
    members = models.ManyToManyField(User, related_name='members', blank=True)
    required_abilities = models.ManyToManyField(Ability, related_name='required_abilities', blank=True, null=True)

    def __str__(self):
        return self.title


class Task(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    description = models.TextField()
    member = models.ForeignKey(User, blank=True, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.description


class Meeting(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    date = models.DateTimeField(blank=True, null=True)
    time = models.DurationField(blank=True, null=True)
    name = models.CharField(max_length=128)
    description = models.TextField()

    def __str__(self):
        return self.name


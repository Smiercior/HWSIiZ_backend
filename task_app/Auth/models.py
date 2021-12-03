from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    BHPCourse = models.BooleanField(default=False)
    Abilities = models.CharField(max_length=64)
    def __str__(self):
        return self.email
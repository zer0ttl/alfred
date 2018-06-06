from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import datetime

# Create your models here.


class CustomUser(AbstractUser):
    name = models.CharField(max_length=255, blank=True)
    birth_year = models.IntegerField(default=datetime.now().year - 18)

    def __str__(self):
        return self.email

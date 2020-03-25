from django.db import models
from django.contrib.auth.models import User


# custom token model
class Token(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    token = models.CharField(max_length=250)

    def __str__(self):
        return self.token



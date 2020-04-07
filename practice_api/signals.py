# django
from django.conf import settings
from django.dispatch import receiver
from django.contrib.auth.models import User
from django.db.models.signals import post_save

# DRF
from rest_framework.authtoken.models import Token


# @receiver() decorator receives the signals before/after creation of an object

# post_save = after creation of an object
# sender = which model is sending the signal
@receiver(post_save, sender=User)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    # instance = data, that came from signals sent by Model
    # created = initially False, but while an object creates, created will be True

    # if created = True
    if created:
        token = Token.objects.create(user=instance)
        print(token)


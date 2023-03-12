from django.db import models
from django.contrib.auth.models import User
from base.models import BaseModel
from django.db.models.signals import post_save
from django.dispatch import receiver
import uuid
from base.emails import send_account_activation_email

class Image(models.Model):
    caption = models.CharField(max_length=100)
    image = models.ImageField(upload_to="MyImage")
    def __str__(self) -> str:
        return self.caption

class Profile(BaseModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    address = models.CharField(max_length=200)
    country = models.CharField(max_length=200)
    state = models.CharField(max_length=200)
    city = models.CharField(max_length=200)

# @receiver(post_save, sender=User)
# def send_email_token(sender, instance, created, **kwargs):
#     try:
#         if created:
#             email_token = str(uuid.uuid4())
#             email =instance.email
#             send_account_activation_email(email, email_token)
#     except Exception as e:
#         print(e)



import uuid

from django.db import models

class BaseModel(models.Model):
    uid = models.UUIDField(primary_key=True, editable=False,default=uuid.uuid4)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    status = models.BooleanField(default=True)

    class Meta:
        abstract = True
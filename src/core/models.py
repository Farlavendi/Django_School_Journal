import uuid

from django.db import models


class Base(models.Model):
    id = models.UUIDField(
        primary_key=True,
        editable=False,
        default=uuid.uuid4,
        db_index=True,
    )

    class Meta:
        abstract = True
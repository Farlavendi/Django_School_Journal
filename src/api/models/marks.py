import uuid

from django.db import models
from django.utils.translation import gettext_lazy as _

from core import settings
from . import AbstractBaseModel

User = settings.AUTH_USER_MODEL


class Marks(AbstractBaseModel):
    __tablename__ = "marks"

    id = models.UUIDField(
        primary_key=True,
        editable=False,
        default=uuid.uuid4,
        db_index=True,
    )
    student = models.OneToOneField(
        to="Student",
        on_delete=models.CASCADE,
        related_name="marks",
        db_column="student_id",
        db_index=True,
        verbose_name=_("Student"),
    )
    maths = models.IntegerField(null=True, blank=True)
    english = models.IntegerField(null=True, blank=True)
    physics = models.IntegerField(null=True, blank=True)
    chemistry = models.IntegerField(null=True, blank=True)
    history = models.IntegerField(null=True, blank=True)
    geography = models.IntegerField(null=True, blank=True)
    literature = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return f"Marks(student_id={self.student.id})"

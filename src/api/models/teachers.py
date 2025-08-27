import uuid

from django.db import models
from django.utils.translation import gettext_lazy as _

from core import settings
from . import AbstractBaseModel, Class

User = settings.AUTH_USER_MODEL


class SubjectEnum(models.TextChoices):
    MATH = "MATH", _("Math")
    ENGLISH = "ENGLISH", _("English")
    PHYSICS = "PHYSICS", _("Physics")
    CHEMISTRY = "CHEMISTRY", _("Chemistry")
    HISTORY = "HISTORY", _("History")
    GEOGRAPHY = "GEOGRAPHY", _("Geography")
    LITERATURE = "LITERATURE", _("Literature")


class Teacher(AbstractBaseModel):
    __tablename__ = "teachers"

    id = models.UUIDField(
        primary_key=True,
        editable=False,
        default=uuid.uuid4,
        db_index=True,
    )
    user = models.OneToOneField(
        to=User,
        on_delete=models.CASCADE,
        related_name="teacher",
        db_column="user_id",
        verbose_name=_("User"),
    )

    _class = models.OneToOneField(
        to=Class,
        on_delete=models.CASCADE,
        related_name="teacher",
        db_column="class_id",
        verbose_name=_("Class"),
    )

    subject = models.CharField(
        max_length=20,
        choices=SubjectEnum.choices,
        null=True,
        blank=True,
        default="",
        verbose_name=_("Subject"),
        db_index=True,
    )

    @property
    def has_subject(self) -> bool:
        return self.subject is not None

    class Meta:
        verbose_name = _("Teacher")
        verbose_name_plural = _("Teachers")


    def __str__(self):
        return f"Teacher(user_id={self.user.id}, class_id={self._class.id}, subject={self.subject})"

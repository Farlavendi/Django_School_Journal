import uuid

from django.db import models
from django.utils.translation import gettext_lazy as _

from core import settings
from . import AbstractBaseModel, Class

User = settings.AUTH_USER_MODEL


class Student(AbstractBaseModel):
    __tablename__ = "students"

    id = models.UUIDField(
        primary_key=True,
        editable=False,
        default=uuid.uuid4,
        db_index=True,
    )
    user = models.OneToOneField(
        to=User,
        on_delete=models.CASCADE,
        related_name="student",
        db_column="user_id",
        verbose_name=_("User"),
    )
    _class = models.ForeignKey(
        to=Class,
        on_delete=models.CASCADE,
        related_name="students",
        db_column="class_id",
        verbose_name=_("Class"),
    )

    class Meta:
        verbose_name = _("Student")
        verbose_name_plural = _("Students")

    def __str__(self):
        return f"Student(user_id={self.user.id}, class_num={self._class.number})"

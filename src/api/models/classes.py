import uuid

from django.core.validators import RegexValidator
from django.db import models
from django.utils.translation import gettext_lazy as _

from . import AbstractBaseModel


class Class(AbstractBaseModel):
    __tablename__ = "classes"

    id = models.UUIDField(
        primary_key=True,
        editable=False,
        default=uuid.uuid4,
        db_index=True,
    )
    code = models.CharField(
        unique=True,
        db_index=True,
        validators=[
            RegexValidator(
                regex=r"^[1-9]\d?[A-Z]$",
                message="Code must be 1 or 2 digits (not starting with 0) followed by a capital letter (e.g., 1A, 12B).",
            )
        ],
        verbose_name=_("Class number")
    )

    class Meta:
        verbose_name = _("Class")
        verbose_name_plural = _("Classes")

    def __str__(self):
        return f"Class №{self.code}"

from django.db import models
from django.utils.translation import gettext_lazy as _

from core import settings

User = settings.AUTH_USER_MODEL


class Class(models.Model):
    number = models.IntegerField(verbose_name=_("Class number"))

    class Meta:
        indexes = (models.Index(fields=["number"]),)
        verbose_name = _("Class")
        verbose_name_plural = _("Classes")


class Student(models.Model):
    name = models.CharField(verbose_name=_("Student's name"), max_length=100)
    _class = models.ForeignKey(
        verbose_name=_("Class"),
        to=Class,
        on_delete=models.CASCADE,
        related_name=_("students"),
    )
    user = models.ForeignKey(
        verbose_name=_("User"),
        to=User,
        on_delete=models.CASCADE,
    )

    class Meta:
        indexes = (models.Index(fields=("name",)), models.Index(fields=("_class",)))
        verbose_name = _("Student")
        verbose_name_plural = _("Students")

    def __str__(self) -> str:
        return f"{self.name} is in {self._class} class."


class Teacher(models.Model):
    name = models.CharField(verbose_name=_("Teacher's name"), max_length=100)
    _class = models.OneToOneField(
        verbose_name=_("Class"), to=Class, on_delete=models.CASCADE
    )

    user = models.ForeignKey(
        verbose_name=_("User"),
        to=User,
        on_delete=models.CASCADE,
    )

    class Meta:
        indexes = (models.Index(fields=("name",)), models.Index(fields=("_class",)))
        verbose_name = _("Teacher")
        verbose_name_plural = _("Teachers")


def __str__(self) -> str:
    return f"{self.name} is a teacher in {self._class} class."

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

from core.models import Base
from . import managers


class RoleEnum(models.TextChoices):
    STUDENT = "STUDENT", _("Student")
    TEACHER = "TEACHER", _("Teacher")


class User(Base, AbstractUser):
    __tablename__ = "users"

    email = models.EmailField(unique=True, db_index=True, verbose_name=_("Email address"))
    username = models.CharField(
        max_length=50,
        unique=True,
        help_text=_("Required. 50 characters or fewer. Letters, digits, and spaces only."),
        validators=[],
        error_messages={
            "unique": _("A user with that username already exists."),
        },
        verbose_name=_("Username"),
    )
    password = models.CharField(
        max_length=150,
        verbose_name=_("Password")
    )
    first_name = models.CharField(max_length=100, verbose_name=_("First name"))
    second_name = models.CharField(max_length=100, null=True , verbose_name=_("Second name"))

    last_name = models.CharField(max_length=100, verbose_name=_("Last name"))

    role = models.CharField(
        max_length=50,
        choices=RoleEnum.choices,
        default=RoleEnum.STUDENT,
        verbose_name=_("User's role"),
    )
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    is_verified = models.BooleanField(default=False)


    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username", "password", "first_name", "last_name", "role"]

    objects = managers.UserManager()

    class Meta:
        verbose_name = _("User")
        verbose_name_plural = _("Users")

    def __str__(self):
        return f"User(id={self.id}, username={self.username}, email={self.email})"

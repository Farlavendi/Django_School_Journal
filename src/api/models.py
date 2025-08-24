from django.core.validators import RegexValidator
from django.db import models
from django.utils.translation import gettext_lazy as _

from core import settings
from core.models import Base

User = settings.AUTH_USER_MODEL


class SubjectEnum(models.TextChoices):
    MATH = "MATH", _("Math")
    ENGLISH = "ENGLISH", _("English")
    PHYSICS = "PHYSICS", _("Physics")
    CHEMISTRY = "CHEMISTRY", _("Chemistry")
    HISTORY = "HISTORY", _("History")
    GEOGRAPHY = "GEOGRAPHY", _("Geography")
    LITERATURE = "LITERATURE", _("Literature")


class Class(Base):
    __tablename__ = "classes"

    code = models.CharField(
        unique=True,
        db_index=True,
        validators=[
            RegexValidator(
                regex=r"^\d{1,2}[A-Z]$",
                message="Code must be 1 or 2 digits followed by a capital letter (e.g., 1A, 12B).",
            )
        ],
        verbose_name=_("Class number")
    )

    class Meta:
        verbose_name = _("Class")
        verbose_name_plural = _("Classes")

    def __str__(self):
        return f"Class №{self.code}"


class Student(Base):
    __tablename__ = "students"

    user = models.OneToOneField(
        to=User,
        on_delete=models.CASCADE,
        related_name="student",
        db_column="user_id",
        verbose_name=_("User"),
    )

    _class = models.OneToOneField(
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


class Teacher(Base):
    __tablename__ = "teachers"

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


class Marks(Base):
    student = models.ForeignKey(
        to=Student,
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
__all__ = ["AbstractBaseModel", "User"]

from .base import AbstractBaseModel
from users.models import User
from .students import Student
from .teachers import Teacher
from .classes import Class

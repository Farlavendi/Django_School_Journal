from django.db import models


class Class(models.Model):
    number = models.IntegerField()

    def __str__(self):
        return self.number


class Student(models.Model):
    name = models.CharField(max_length=100)
    _class = models.ForeignKey(Class, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name} is in {self._class} class.'


class Teacher(models.Model):
    name = models.CharField(max_length=100)
    _class = models.OneToOneField(Class, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name} is a teacher in {self._class} class.'

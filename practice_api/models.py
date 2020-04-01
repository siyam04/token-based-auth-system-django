from django.db import models
from django.contrib.auth.models import User


class Student(models.Model):
    std_name = models.CharField(max_length=100, null=True, blank=True)
    std_roll = models.PositiveSmallIntegerField(null=True, blank=True)
    std_class = models.CharField(max_length=100, null=True, blank=True)

    class Meta:
        ordering = ['-id']
        verbose_name_plural = 'Students'

    def __str__(self):
        return self.std_name


class Attendance(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, null=True, blank=True)
    date = models.DateField(auto_now_add=True, null=True, blank=True)
    status = models.BooleanField()

    class Meta:
        ordering = ['-id']
        verbose_name_plural = 'Attendance'

    def __str__(self):
        return str(self.student.std_roll)


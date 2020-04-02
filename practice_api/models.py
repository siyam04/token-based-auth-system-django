# django packages
from django.db import models
from django.contrib.auth.models import User


class Student(models.Model):
    std_name = models.CharField(max_length=100, null=True, blank=True)
    std_roll = models.PositiveSmallIntegerField(null=True, blank=True)
    std_class = models.PositiveSmallIntegerField(null=True, blank=True)

    class Meta:
        ordering = ['-id']
        verbose_name_plural = 'Students'
        unique_together = ['std_roll', 'std_class']

    def __str__(self):
        return self.std_name


# model manager for Attendance class
class AttendanceManager(models.Manager):
    def set_attendance(self, roll_no, class_no):
        std_obj = Student.objects.get(std_roll=roll_no, std_class=class_no)
        att_obj = Attendance.objects.create(student=std_obj, status=True)
        return att_obj


class Attendance(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, null=True, blank=True)
    date = models.DateField(auto_now_add=True, null=True, blank=True)
    status = models.BooleanField()

    # model manager object
    objects = AttendanceManager()

    class Meta:
        ordering = ['-id']
        verbose_name_plural = 'Attendance'
        unique_together = ['student', 'date']

    def __str__(self):
        return str(self.student.std_roll)


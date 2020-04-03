from rest_framework import serializers

from .models import Student, Attendance


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'


# class AttendanceSerializer(serializers.ModelSerializer):
#     # students = serializers.PrimaryKeyRelatedField(read_only=True)
#
#     class Meta:
#         model = Attendance
#         # fields = ('student', 'date', 'status')
#         fields = '__all__'

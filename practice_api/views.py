# django packages
from pprint import pprint
from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView

# DRF packages
from rest_framework import status
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

# my app
from .models import Student, Attendance
from .serializers import StudentSerializer, AttendanceSerializer


# API: creating attendance
class StudentAttendance(APIView):
    # GET method
    def get(self, request, roll_no=None, class_no=None):
        # Note: Attendance.objects, here 'objects' is custom model manager objects (CREATE)
        attendance = Attendance.objects.set_attendance(roll_no, class_no)
        print('TEST DATA: ', attendance)

        # if attendance:
        #     serialized_attendance = AttendanceSerializer(attendance)
        #     return Response(serialized_attendance.data, status=status.HTTP_302_FOUND)
        # else:
        #     return Response({'message': 'attendance not found!'}, status=status.HTTP_404_NOT_FOUND)

        data = {
            'message': 'attendance created successfully!',
            'student_name': attendance.student.std_name,
            'roll': attendance.student.std_roll,
            'class': attendance.student.std_class,
            'date': attendance.date,
            'status': attendance.status
        }
        return Response(data=data, status=status.HTTP_201_CREATED)


# API: filtered students according to class number
class FilteredStudent(APIView):
    # GET method
    def get(self, request, class_no=None):
        students = Student.objects.filter(std_class=class_no)
        if students:
            serialized_students = StudentSerializer(students, many=True)
            return Response(data=serialized_students.data, status=status.HTTP_302_FOUND)
        else:
            return Response({'message': 'students not found!'}, status=status.HTTP_404_NOT_FOUND)


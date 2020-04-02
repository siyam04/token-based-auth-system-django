# django packages
from pprint import pprint
from django.shortcuts import render

# DRF packages
from rest_framework import status
from rest_framework.decorators import api_view, APIView
from rest_framework.response import Response

# my models
from .models import Student, Attendance


# FBV
@api_view(['GET'])
def student_attendance(request, roll_no, class_no):
    try:
        # note: Attendance.objects, here 'objects' is custom model manager objects
        attendance = Attendance.objects.set_attendance(roll_no, class_no)
        data = {
            'message':
                f"attendance created for: {attendance.student.std_name}, "
                f"roll: {attendance.student.std_roll}, "
                f"class: {attendance.student.std_class}"
        }
        return Response(data=data, status=status.HTTP_201_CREATED)

    except Exception as err:
        pprint(err)
        return Response({'status': 'already exists!'}, status=status.HTTP_208_ALREADY_REPORTED)

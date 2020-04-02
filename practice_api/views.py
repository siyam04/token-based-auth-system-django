# django packages
from pprint import pprint
from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView

# DRF packages
from rest_framework import status
from rest_framework.decorators import api_view, APIView
from rest_framework.response import Response

# my models
from .models import Student, Attendance


# FBV api
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


# FBV template
def attendance_count(request):
    class_number = request.GET.get('class_number', None)

    if class_number:
        students = Student.objects.filter(std_class=class_number)

        if students:
            context = {'students': students}
            template = 'attendance_count.html'
            messages.success(request, 'Student Found!', extra_tags='html_safe')
            return render(request, template, context)
        else:
            return HttpResponse('Not Found!')
    else:
        template = 'attendance_count.html'
        context = {}
        return render(request, template, context)



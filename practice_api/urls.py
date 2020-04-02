from django.urls import path

# custom app
from .views import (

    StudentAttendance,
    attendance_count,
)


urlpatterns = [

    # attendance create api
    path('attendance/<int:roll_no>/<int:class_no>/', StudentAttendance.as_view()),

    # attendance count
    path('att-count/', attendance_count, name='att-count'),

]

from django.urls import path

# custom app
from .views import (

    student_attendance,
    attendance_count,
)


urlpatterns = [

    # attendance create api
    path('attendance/<int:roll_no>/<int:class_no>/', student_attendance),

    # attendance count
    path('att-count/', attendance_count, name='att-count'),

]

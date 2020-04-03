from django.urls import path

# custom app
from .views import (

    StudentAttendance,
    FilteredStudent,
)


urlpatterns = [

    # create attendance api
    path('create-attendance/<int:roll_no>/<int:class_no>/', StudentAttendance.as_view()),

    # filtered students api by class number
    path('filtered-student/<int:class_no>/', FilteredStudent.as_view()),

]



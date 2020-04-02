from django.urls import path

# custom app
from .views import student_attendance


urlpatterns = [

    # attendance create api
    path('attendance/<int:roll_no>/<int:class_no>/', student_attendance),

]

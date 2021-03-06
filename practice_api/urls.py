from django.urls import path

# custom app
from .views import (

    Login,
    Signup,
    Logout,

    Dashboard,
    AllStudent,
    FilteredStudent,
    StudentAttendance,

    JWTView,
)


urlpatterns = [

    # static dashboard
    path('dashboard/', Dashboard.as_view(), name='dashboard'),

    # API: all students
    path('students/', AllStudent.as_view()),

    # API: create attendance
    path('create-attendance/<int:roll_no>/<int:class_no>', StudentAttendance.as_view()),

    # API: filtered students by class number
    path('filtered-student/<int:class_no>', FilteredStudent.as_view()),

    # API: DRF token based auth system using signals
    path('sign-up/', Signup.as_view()),
    path('login/', Login.as_view()),
    path('logout/', Logout.as_view()),

    # API: JWT testing
    path('jwt-testing/', JWTView.as_view()),


]





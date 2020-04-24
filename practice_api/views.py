# django packages
from pprint import pprint
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.views.generic import TemplateView

# DRF packages
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token

# DRF validation
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import (

    TokenAuthentication,
    BasicAuthentication,
    SessionAuthentication,
)

# my app
from .models import Student, Attendance
from .serializers import (

    StudentSerializer,
    UserSerializer,
    TokenSerializer,
)


# static view
class Dashboard(TemplateView):
    template_name = 'dashboard.html'


# API: all students
class AllStudent(APIView):
    def get(self, request):
        students = Student.objects.all().order_by('std_roll')
        if students:
            serialized_students = StudentSerializer(students, many=True)
            return Response(data=serialized_students.data, status=status.HTTP_302_FOUND)
        else:
            return Response({'message': 'students not found!'}, status=status.HTTP_404_NOT_FOUND)


# API: creating attendance
class StudentAttendance(APIView):
    def get(self, request, roll_no=None, class_no=None):
        try:
            # Note: Attendance.objects, here 'objects' is custom model manager objects (CREATE)
            attendance = Attendance.objects.set_attendance(roll_no, class_no)

            if attendance:
                data = {
                    'message': 'attendance created successfully!',
                    'student_name': attendance.student.std_name,
                    'roll': attendance.student.std_roll,
                    'class': attendance.student.std_class,
                    'date': attendance.date,
                    'status': attendance.status
                }
                return Response(data=data, status=status.HTTP_201_CREATED)

            else:
                return Response({'message': 'student not found!'}, status=status.HTTP_404_NOT_FOUND)

        except Exception as err:
            pprint(err)
            return Response({'message': 'already exists!'}, status=status.HTTP_400_BAD_REQUEST)


# API: filtered students according to class number
class FilteredStudent(APIView):
    def get(self, request, class_no=None):
        students = Student.objects.filter(std_class=class_no)
        if students:
            serialized_students = StudentSerializer(students, many=True)
            return Response(data=serialized_students.data, status=status.HTTP_302_FOUND)
        else:
            return Response({'message': 'students not found!'}, status=status.HTTP_404_NOT_FOUND)


##################################### DRF Token-based auth starts from here #####################################


# API: Signup and Token generating using Signals
class Signup(APIView):
    def post(self, request):
        # getting api data
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')

        # if data available
        if username and email and password:
            # user creation
            user = User.objects.create_user(
                username=username,
                email=email,
                password=password,
                first_name=first_name,
                last_name=last_name,
            )

            # DRF token generating
            # token = Token.objects.create(user=user)
            # token = create_auth_token()

            """data section"""
            # serialized user
            serialized_user = UserSerializer(user)

            # serialized token
            # serialized_token = TokenSerializer(token)
            # print('Serialized Token: ', serialized_token)

            # success response
            # return Response(serialized_token.data, status=status.HTTP_201_CREATED)
            return Response(serialized_user.data, status=status.HTTP_201_CREATED)

        # failed response
        else:
            return Response({'message': 'Signup Failed! Data Not Found!'}, status=status.HTTP_404_NOT_FOUND)


# APi: Login
class Login(APIView):
    # authentication_classes = [TokenAuthentication, ]
    # authentication_classes = [SessionAuthentication, BasicAuthentication]
    # permission_classes = [IsAuthenticated]
    # permission_classes = [IsAuthenticated | ReadOnly]

    def post(self, request):
        # getting api data
        username = request.POST.get('username')
        password = request.POST.get('password')

        token = request.headers['Token']

        # if data available
        if username and password and token:
            authenticated = authenticate(username=username, password=password)
            user_token = Token.objects.get(user=authenticated)

            # if tokenized user
            if user_token:
                return Response(
                    {'message': f"Login Successful for '{authenticated}', Token: '{user_token}'"},
                    status=status.HTTP_200_OK
                )

            # if not
            else:
                return Response({'message': 'Login Failed!'}, status=status.HTTP_401_UNAUTHORIZED)

        # if data not available
        else:
            return Response({'message': 'Data Not Found!'}, status=status.HTTP_404_NOT_FOUND)


# APi: Logout
class Logout(APIView):
    authentication_classes = [TokenAuthentication, ]

    def get(self, request):
        # getting token
        token = request.headers['Token']

        # if token available
        if token:

            # matching api token with db token
            matched_token = Token.objects.get(key=token)

            # deleting db token
            if matched_token:
                matched_token.delete()

                # if succeed
                return Response({'message': 'Logout Successful!'}, status=status.HTTP_200_OK)

            # if token not matched
            else:
                return Response({'message': 'Token Not Matched!'}, status=status.HTTP_401_UNAUTHORIZED)

        # if not succeed
        else:
            return Response({'message': 'Token Not Found!'}, status=status.HTTP_404_NOT_FOUND)


###################################### jWT testing #############################################################

class JWTView(APIView):
    permission_classes = (IsAuthenticated,)
    # authentication_classes = (TokenAuthentication,)

    def get(self, request):
        content = {'message': 'JWT testing!'}
        return Response(content)


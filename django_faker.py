import os, django, random

# Configure settings for project
# Need to run this before calling models from application!
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'root.settings')
django.setup()

# faker
from faker import Faker
# my models
from practice_api.models import Student, Attendance


# creating Faker object
fake_data = Faker()

# my custom classes
# classes = ['Class 1', 'Class 2', 'Class 3']
classes = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


# 1st, creating student object with fake data
def add_student():
    student = Student.objects.get_or_create(
        std_name=fake_data.name(),
        std_roll=random.randint(1, 20),
        std_class=random.choice(classes),
    )[0]

# note: [0] = I use get_or_create() method, if student object already exists then get from first index.
# If not, then create the student object.

    # saving student obj
    student.save()

    # returning student obj
    return student


# populating the Student and Attendance class
def populate(n):
    for entry in range(n):

        # calling add_student() method for creating student object first
        student = add_student()

        # 2nd, creating attendance object with previously created student object
        Attendance.objects.get_or_create(
            student=student,
            date=fake_data.date(),
            status=fake_data.boolean()
        )


# calling the populate() method
if __name__ == '__main__':
    print("Populating the Database, Please Wait...")
    populate(5)
    print('Populating Complete!')


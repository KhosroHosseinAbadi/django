import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "blog.settings")

import django
django.setup()

from random import randint
from faker import Faker

from schools.models import School
from students.models import Student


faker = Faker()


def populate():
    for _ in range(8):
        principal = faker.name()
        name = principal + " School"
        location = faker.country()
        school = School(name=name, principal=principal, location=location)
        school.save()
        for _ in range(randint(10, 20)):
            name = faker.name().split()[0]
            age = randint(10, 20)
            student = Student(name=name, age=age, school=school)
            student.save()


if __name__ == "__main__":
    print("Start populating...")
    populate()
    print("End populationg...")

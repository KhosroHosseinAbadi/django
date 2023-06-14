import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'level6.settings')
import django
django.setup()

from random import randint
from faker import Faker
from app1.models import School, Student

faker = Faker()

def populate():
    for _ in range(4):
        principal = faker.name()
        name = principal + ' School'
        location = faker.country()
        school = School(name=name, principal=principal, location=location)
        school.save()
        for _ in range(10):
            name = faker.name().split()[0]
            age = randint(10, 20)
            student = Student(name=name, age=age, school=school)
            student.save()


if __name__ == '__main__':
    print('Start populating...')
    populate()
    print('End populationg...')


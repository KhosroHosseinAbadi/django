# This lines must be on top the code.

# set default for environment variable
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'level2.settings')

# setup django apps
import django
django.setup()

# Start the code:

import random
from faker import Faker
from app1.models import Webpage, AccessRecord, Topic

faker = Faker()
topic_names = ['Search', 'Social', 'Market', 'News', 'Games']

def populate(n=5):
    
    for entry in range(n):
    
        topic = Topic.objects.get_or_create(name=random.choice(topic_names))[0]

        web_name = faker.company()
        web_url = faker.url()
        webpage = Webpage.objects.get_or_create(name=web_name, url=web_url, topic=topic)[0]

        date = faker.date()
        acc_rec = AccessRecord.objects.get_or_create(webpage=webpage, date=date)[0]

if __name__ == '__main__':

    print('Populating starts...')
    populate()
    print('Populating ends!')

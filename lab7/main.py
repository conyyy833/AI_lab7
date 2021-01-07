import csv
import time
from random import random
from faker import Faker


class hospital:
    name = ""
    grade = ""
    scale = ""
    online_consultation = ""
    main_departments = ""
    number_of_patients = ""
    service = ""
    quality = ""
    effectiveness = ""


    def __init__(self,a):
        fake = Faker("En")
        Faker.seed(time.time())
        self.name = fake.word()
        self.grade = fake.int()
        self.scale = fake.int()
        self.online_consultation = fake.isinstance()
        self.main_departments = fake.word()
        self.number_of_patients = fake.int()
        self.service = fake.word(ext_word_list=['Best', 'Good', 'General','Ok'])
        self.quality = fake.word(ext_word_list=['Best', 'Good', 'General','Ok'])
        self.effectiveness = fake.word(ext_word_list=['Best', 'Good', 'General','Ok'])

    def __init__(self, b):
        fake = Faker("En")
        Faker.seed(time.time())
        self.name = fake.word()
        self.grade = fake.int()
        self.scale = fake.int()
        self.online_consultation = fake.isinstance()
        self.main_departments = fake.word()
        self.number_of_patients = fake.int()
        self.service = fake.word(ext_word_list=['Best', 'Good', 'General','Ok'])
        self.quality = fake.word(ext_word_list=['Best', 'Good', 'General','Ok'])
        self.effectiveness = fake.word(ext_word_list=['Best', 'Good', 'General','Ok'])


def GenerateData():
    with open('hospital.csv', 'w', newline='', encoding="utf-8") as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=' ',
                                quotechar='|', quoting=csv.QUOTE_MINIMAL)
        for i in range(0, 100):
            hospital = hospital()
            spamwriter.writerow([hospital.name, hospital.grade, hospital.scale,
                                 hospital.online_consultation, hospital.main_departments,
                                 hospital.number_of_patient,hospital.service,
                                 hospital.quality,hospital.effectiveness])


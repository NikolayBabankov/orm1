import csv

from django.core.management.base import BaseCommand
from phones.models import Phone


class Command(BaseCommand):
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        with open('phones.csv', 'r') as csvfile:

            phone_reader = csv.reader(csvfile, delimiter=';')
            # пропускаем заголовок
            next(phone_reader)

            for line in phone_reader:
                id_phone = line[0]
                name_phone = line[1]
                price = int(line[3])
                image = line[2]
                release_date = line[4]
                lte_exists = line[5]
                tmp_str = name_phone.split()
                slug = '_'.join(tmp_str)
                phone = Phone(id = id_phone, name = name_phone,price = price, image = image,release_date= release_date,
                lte_exists = lte_exists,slug= slug )
                phone.save()

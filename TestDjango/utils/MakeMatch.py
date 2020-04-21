import os
import django
from faker import Faker

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'TestDjango.settings')
django.setup()
fake_gen = Faker()
from match.models import Match


def write_match_table():
    try:  # Генерируем рандомные данные для модели Match и сохраняем в db
        [Match(first_name=fake_gen.first_name(), last_name=fake_gen.last_name(),
               age=fake_gen.random_int(0, 100), gender=fake_gen.random_int(0, 1)).save() for _ in range(10)]

    except Exception as e:
        print('Error:', e)

    else:
        print('Success')


if __name__ == '__main__':
    write_match_table()

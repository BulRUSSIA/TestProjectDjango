import os
import django
from faker import Faker
import requests

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'TestDjango.settings')
django.setup()
fake_gen = Faker()
from human.models import Human

def write_human_table():
    try:  # Генерируем рандомные данные для модели Humans и сохраняем в db
        [Human(avatar=save_avatar(fake_gen.image_url()), first_name=fake_gen.first_name(),
               last_name=fake_gen.last_name(),
               age=fake_gen.random_int(0, 100), gender=fake_gen.random_int(0, 1)).save() for _ in range(10)]
    except Exception as e:
        print('Error:', e)


def save_avatar(url):  # cохраняем изображения из fake_url()
    try:
        filename = fake_gen.last_name() + '.png'
        response = requests.get(url)
        file = open(filename, "wb")
        file.write(response.content)
        file.close()
        return filename
    except Exception as e:
        print('save_avatar_error:', e)


if __name__ == '__main__':
    write_human_table()

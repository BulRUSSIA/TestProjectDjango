from django.db import models


class Match(models.Model):
    """
    Создание модели Match

    """
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)

    age = models.IntegerField()
    GENDER_CHOICES = [
        (0, 'Male'),
        (1, 'Female'),
    ]
    gender = models.IntegerField(choices=GENDER_CHOICES)

    def __str__(self):
        return self.first_name

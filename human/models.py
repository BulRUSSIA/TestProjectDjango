from django.db import models
from match.models import Match


class Human(models.Model):
    """
       Создание модели Human
       В качестве внешнего ключа указываем модель Match для связи
       в бд

       """
    avatar = models.ImageField(blank=True, upload_to='human_avatar/')
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    match = models.ForeignKey(Match, on_delete=models.CASCADE, null=True)
    age = models.IntegerField()
    GENDER_CHOICES = [
        (0, 'Male'),
        (1, 'Female'),
    ]
    gender = models.IntegerField(choices=GENDER_CHOICES)

    def __str__(self):
        return self.first_name

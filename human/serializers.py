from rest_framework.serializers import ModelSerializer
from human.models import Human


# todo сериализовать модель match,чтоб показывался не только id,но и все поля сущности,сделаь комментарии
class HumanSerializer(ModelSerializer):
    class Meta:

        """
        Сериализуем выбранную модель Human
        В качестве fields указываем нужные поля

        """
        model = Human
        fields = ['first_name', 'last_name', 'avatar', 'age', 'gender', 'id', 'match']

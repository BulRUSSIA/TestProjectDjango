from rest_framework.serializers import ModelSerializer
from human.models import Human


class HumanSerializer(ModelSerializer):
    class Meta:

        """
        Сериализуем выбранную модель Human
        В качестве fields указываем нужные поля

        """
        model = Human
        fields = ['first_name', 'last_name', 'avatar', 'age', 'gender', 'id', 'match']

from rest_framework.serializers import ModelSerializer
from human.serializers import HumanSerializer
from match.models import Match


class MatchSerializer(ModelSerializer):
    """
          Для отображения всех полей сущности Human

          """
    human_set = HumanSerializer(many=True)

    class Meta:
        """
              Сериализуем выбранную модель Match
              В качестве fields указываем нужные поля

              """
        model = Match
        fields = ['first_name', 'last_name', 'age', 'gender', 'human_set', 'id']

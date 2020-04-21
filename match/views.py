from rest_framework import viewsets
from match.models import Match
from match.serializers import MatchSerializer


class MatchList(viewsets.ModelViewSet):
    """
        Создаем класс endpoint для api Match.
        Указываем в полях queryset(запрос для обращения к бд)
        и собственный класс сериализатор.

        """
    queryset = Match.objects.all()
    serializer_class = MatchSerializer
    http_method_names = ['get', 'post', 'put', 'delete']

from rest_framework import viewsets
from .models import Human
from .serializers import HumanSerializer


class HumansList(viewsets.ModelViewSet):
    """
    Создаем класс endpoint для api human.
    Указываем в полях queryset(запрос для обращения к бд)
    и собственный класс сериализатор.

    """
    queryset = Human.objects.all()
    serializer_class = HumanSerializer
    http_method_names = ['get', 'post', 'put', 'delete']


from django.http import JsonResponse
from rest_framework import viewsets
from CBC_SERVER.serializers import *
from cbc_app.models import *


response_data = {}
response_data['result'] = 'error'

class userViewSet(viewsets.ModelViewSet):

    queryset = user.objects.all()
    serializer_class = userSerializer


class coffee_breakViewSet(viewsets.ModelViewSet):

    queryset = coffee_break.objects.all()
    serializer_class = coffee_breakSerializer


def test(resuest):
    print("test")
    return JsonResponse({'Hello': 'VICTOIRE! et Daouda!'})


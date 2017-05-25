from rest_framework import serializers
from cbc_app.models import *

class userSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = user
        #fields = ('user_name')
        fields = '__all__'


class coffee_breakSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = coffee_break
        fields = ('date', 'time', 'place')
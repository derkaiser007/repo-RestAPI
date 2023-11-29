from rest_framework import serializers
from .models import CatResult

from django.contrib.auth.models import User

class CatResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = CatResult
        fields = ['id', 'first_name', 'last_name', 'cat_score', 'cat_percentile', 'possibility_of_getting_IIM']

class TokenSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password']

    def create(self, validated_data):
        user = User.objects.create(username=validated_data['username'])
        user.set_password(validated_data['password'])
        user.save()
        return user

"""
python manage.py shell
from appapi1.serializers import CatResultSerializer
serializer = CatResultSerializer
print(repr(serializer))
exit()
"""
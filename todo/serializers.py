from .models import ToDoList
from rest_framework import serializers
from django.contrib.auth.models import User


class ToDoListSerializer(serializers.ModelSerializer):
    class  Meta:
        model  = ToDoList
        fields = '__all__'

class RegistationSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def create(self, validated_data):
        user = User.objects.create_user(
            username = validated_data['username'],
            email = validated_data['email'],
        )
        user.set_password(validated_data['password'])
        user.save()
        return user

from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Post, Comment

class UserSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    username = serializers.CharField()
    email = serializers.EmailField()
    password = serializers.CharField()

    def create(self, validate_data):
        instance = User()
        instance.first_name = validate_data.get('first_name')
        instance.last_name = validate_data.get('last_name')
        instance.username = validate_data.get('username')
        instance.email = validate_data.get('email')
        instance.set_password(validate_data.get('password'))
        instance.save()
        return instance

    def validate_username(self, data):
        users = User.objects.filter(username = data)
        if len(users) != 0:
            raise serializers.ValidationError("Este nombre de usuario ya existe, ingrese uno nuevo")
        else:
            return data

class PostSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    name = serializers.CharField()
    description = serializers.CharField()
    fix_id = serializers.IntegerField()

    def create(self, validate_data):
            instance = Post()
            instance.name = validate_data.get('name')
            instance.description = validate_data.get('description')
            instance.fix_id = validate_data.get('fix_id')
            instance.save()
            return instance

class CommentSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    name = serializers.CharField()
    description = serializers.CharField()
    fix_id = serializers.IntegerField()

    def create(self, validate_data):
            instance = Comment()
            instance.name = validate_data.get('name')
            instance.description = validate_data.get('description')
            instance.fix_id = validate_data.get('fix_id')
            instance.save()
            return instance

"""class LikeSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    like = serializers.IntegerField()
    fix_id = serializers.IntegerField()

    def create(self, validate_data):
            instance = Like()
            instance.like = validate_data.get('like')
            instance.fix_id = validate_data.get('fix_id')
            instance.save()
            return instance"""

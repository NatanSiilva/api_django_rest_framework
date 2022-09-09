from rest_framework import serializers
from apps.users.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

    def to_representation(self, instance):
        # super().to_representation(instance)
        return {
            "id": instance["id"],
            "username": instance["username"],
            "email": instance["email"],
            "name": instance["name"],
        }


    def validate_username(self, value):
        if len(value) < 4:
            raise serializers.ValidationError("Username must be at least 3 characters long")
        return value

    def validate(self, data):
        return data            

    def create(self, validated_data):
        return User(**validated_data)

    def update(self, instance, validated_data):
        instance.username = validated_data.get('username', instance.username)
        instance.email = validated_data.get('email', instance.email)
        instance.name = validated_data.get('name', instance.name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.save()
        return instance

# class TestUserSerializer(serializers.Serializer):
#     name = serializers.CharField(max_length=100)
#     email = serializers.EmailField()

#     def validate_name(self, value):
#         if len(value) < 4:
#             raise serializers.ValidationError("Name is too short")
#         return value

#     def validate(self, data):
#         return data

#     def create(self, validated_data):
#         return User.objects.create(**validated_data)

#     def update(self, instance, validated_data):
#         instance.name = validated_data.get('name', instance.name)
#         instance.email = validated_data.get('email', instance.email)
#         instance.save()
#         return instance 
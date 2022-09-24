from rest_framework import serializers
from apps.users.models import User
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


# class UserTokenSerializer(serializers.ModelSerializer):
#     """
#     Serializer for the UserToken model
#     """

#     class Meta:
#         model = User
#         fields = (
#             "id",
#             "username",
#             "email",
#             'last_name',
#         )


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    """
    Custom TokenObtainPairSerializer
    """

    def validate(self, attrs):
        data = super().validate(attrs)

        refresh = self.get_token(self.user)

        data["refresh"] = str(refresh)
        data["access"] = str(refresh.access_token)
        data["username"] = self.user.username
        data["email"] = self.user.email
        data["last_name"] = self.user.last_name

        return data


class CustomUserSerializer(serializers.ModelSerializer):
    """
    Custom User Serializer
    """

    class Meta:
        model = User
        fields = (
            "id",
            "username",
            "email",
            "last_name",
        )


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"

    def create(self, validated_data):
        user = User(**validated_data)
        user.set_password(validated_data["password"])
        user.save()
        return user

    def update(self, instance, validated_data):
        updated_user = super().update(instance, validated_data)
        updated_user.set_password(validated_data["password"])
        updated_user.save()
        return updated_user


class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = User

    def to_representation(self, instance):
        return {
            "id": instance["id"],
            "username": instance["username"],
            "email": instance["email"],
            "name": instance["name"],
            # "password": instance["password"],
        }


class UpdateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            "username",
            "email",
            "name",
            "last_name",
        )


class PasswordSerializer(serializers.Serializer):
    password = serializers.CharField(required=True, write_only=True)
    password1 = serializers.CharField(required=True, write_only=True)

    def validate_password(self, value):
        if len(value) < 6:
            raise serializers.ValidationError("Senha muito curta")
        return value

    def validate_password1(self, value):
        if len(value) < 6:
            raise serializers.ValidationError("Senha muito curta")
        return value

    def validate(self, data):
        if data["password"] != data["password1"]:
            raise serializers.ValidationError({
                "password": "Senhas não conferem"
            })
        return data

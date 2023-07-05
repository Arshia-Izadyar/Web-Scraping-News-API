from rest_framework import serializers

from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth.models import User
from rest_framework.exceptions import ValidationError
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.settings import api_settings
from django.contrib.auth.models import update_last_login


class RegisterUserSerializer(serializers.ModelSerializer):
    email = serializers.CharField(required=True, validators=[UniqueValidator(queryset=User.objects.all())])

    password1 = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ("email", "username", "first_name", "last_name", "email", "password1", "password2")
        extra_kwargs = {"first_name": {"required": True}, "last_name": {"required": True}}

    def validate(self, attrs):
        validate = super().validate(attrs)
        if attrs["password1"] != attrs["password2"]:
            raise ValidationError({"status": "passwods dont match !!! "})
        else:
            return validate

    def create(self, validated_data):
        user = User.objects.create(
            first_name=validated_data["first_name"],
            last_name=validated_data["last_name"],
            email=validated_data["email"],
            username=validated_data["username"],
        )
        user.set_password(validated_data["password1"])
        user.save()
        return user


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)

        refresh = self.get_token(self.user)

        data["refresh"] = str(refresh)
        data["access"] = str(refresh.access_token)
        data["user"] = self.user.get_username()
        data["email"] = self.user.email

        if api_settings.UPDATE_LAST_LOGIN:
            update_last_login(None, self.user)

        return data


class ChangePassWordSerializer(serializers.ModelSerializer):
    old_pass = serializers.CharField()
    new_pass = serializers.CharField(required=True)
    new_pass2 = serializers.CharField(required=True)

    class Meta:
        model = User
        fields = ("old_pass", "new_pass", "new_pass2")

    def validate(self, attrs):
        if attrs["new_pass"] != attrs["new_pass2"]:
            raise ValidationError({"status": "passwods dont match !!! "})
        try:
            password = attrs["new_pass"]
            validate_password(password)
        except ValidationError as e:
            raise serializers.ValidationError({"Error": e})
        return super().validate(attrs)

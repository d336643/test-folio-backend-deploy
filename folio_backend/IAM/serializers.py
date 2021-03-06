from rest_framework import serializers
from rest_framework_simplejwt.exceptions import InvalidToken
from rest_framework_simplejwt.serializers import TokenRefreshSerializer

from .models import MyUser


class RegistrationSerializer(serializers.ModelSerializer):
    # password2 = serializers.CharField(style={"input_type": "password"}, write_only=True)

    class Meta:
        model = MyUser
        fields = ["account", "email", "password"]
        extra_kwargs = {"password": {"write_only": True}}

    def save(self):
        # Simplify the required data
        user = MyUser(
            account=self.validated_data["account"],
            email=self.validated_data["email"],
        )
        password = self.validated_data["password"]

        # # ignore second password confirmation
        # password2 = self.validated_data["password2"]
        # if password != password2:
        #     raise serializers.ValidationError({"password": "Passwords must match."})

        user.set_password(password)
        user.save()
        return user


class PasswordChangeSerializer(serializers.Serializer):
    current_password = serializers.CharField(style={"input_type": "password"}, required=True)
    new_password = serializers.CharField(style={"input_type": "password"}, required=True)

    def validate_current_password(self, value):
        if not self.context["request"].user.check_password(value):
            raise serializers.ValidationError({"current_password": "Does not match"})
        return value


class CookieTokenRefreshSerializer(TokenRefreshSerializer):
    refresh = None

    def validate(self, attrs):
        attrs["refresh"] = self.context["request"].COOKIES.get("refresh_token")
        if attrs["refresh"]:
            return super().validate(attrs)
        else:
            raise InvalidToken("No valid token found in cookie 'refresh_token'")

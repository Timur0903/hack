from rest_framework import serializers
from django.contrib.auth import get_user_model

from account.models import CustomUser

User = get_user_model()



class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(min_length=6, max_length=20, required=True, write_only=True)
    password_confirmation = serializers.CharField(min_length=6, max_length=20, required=True, write_only=True)

    class Meta:
        model = CustomUser
        fields = ('email', 'password', 'password_confirmation', 'username', 'first_name', 'last_name', 'avatar', 'is_staff')

    def validate(self, attrs):
        password = attrs['password']
        password_confirmation = attrs['password_confirmation']
        if password != password_confirmation:
            raise serializers.ValidationError('Пароли должны быть одинаковыми.')

        if password.isdigit() or password_confirmation.isdigit():
            raise serializers.ValidationError('Пароль должен содержать буквы и цифры.')

        return attrs

    def create(self, validated_data):
        password = validated_data.pop('password')
        password_confirmation = validated_data.pop('password_confirmation')  # Удалить password_confirmation
        if password != password_confirmation:
            raise serializers.ValidationError('Пароли должны быть одинаковыми.')
        return CustomUser.objects.create_user(password=password, **validated_data)


class ActivationSerializer(serializers.Serializer):
    code = serializers.CharField(required=True)

    def validate(self, attrs):
        self.code = attrs['code']
        return attrs

    def save(self, **kwargs):
        try:
            user = User.objects.get(activation_code=self.code)
            user.is_active = True
            user.activation_code = ''
            return user  # Вернем обновленного пользователя
        except User.DoesNotExist:
            raise serializers.ValidationError('Неверный код')
class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        exclude = ('password',)

class RegisterPhoneSerializer(serializers.ModelSerializer):
    password = serializers.CharField(min_length=6, max_length=20, required=True, write_only=True)
    password_confirmation = serializers.CharField(min_length=6, max_length=20, required=True, write_only=True)

    class Meta:
        model = User
        fields = ('email', 'password', 'password_confirmation','username', 'first_name', 'last_name', 'username', 'avatar')

    def validate(self, attrs):
        password = attrs['password']
        password_confirmation = attrs.pop('password_confirmation')
        if password != password_confirmation:
            raise serializers.ValidationError(
                'Пароли должны быть похожи'
            )
        if password.isdigit() or password_confirmation.isalpha():
            raise serializers.ValidationError(
                'Пароль должен содержать буквы и цифры'
            )

        return attrs


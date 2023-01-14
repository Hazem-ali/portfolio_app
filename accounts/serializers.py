from rest_framework import serializers
from .models import User


class RegisterSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(
        write_only=True, style={'input_type': 'password'})

    class Meta:
        model = User
        fields = ['username', 'full_name', 'email',
                  'password', 'confirm_password', 'date_of_birth']

        extra_kwargs = {
            'password': {'write_only': True}
        }

    def validate(self, data):
        password = data['password']
        confirm_password = data['confirm_password']
        email = data['email']

        if password != confirm_password:
            raise serializers.ValidationError(
                {'error': "Passwords didn't match"})
        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError(
                {'error': "email already exists"})

        return data

    def save(self):
        password = self.validated_data['password']

        account = User(
            email=self.validated_data['email'],
            username=self.validated_data['username'],
            full_name=self.validated_data['full_name'],
            date_of_birth=self.validated_data.get('date_of_birth', None),
            image=self.validated_data.get('image', None),
        )

        account.set_password(password)
        account.save()

        return account

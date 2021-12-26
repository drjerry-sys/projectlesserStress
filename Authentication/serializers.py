from Authentication.models import MyUser
from rest_framework import serializers

class CreateUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = MyUser
        fields = ('email', 'user_name', 'password', 'first_name')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance
from rest_framework import serializers
from .models import Correspondent


class CorrespondentSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    last_name = serializers.CharField(max_length=50)
    first_name = serializers.CharField(max_length=50)
    email_address = serializers.EmailField()
    phone_number = serializers.CharField(max_length=50)
    address_id = serializers.IntegerField(read_only=True)

    def create(self, validated_data):
        return Correspondent.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.id = validated_data.get('id', instance.id)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.email_address = validated_data.get('email_address', instance.email_address)
        instance.phone_number = validated_data.get('phone_number', instance.phone_number)
        instance.address_id = validated_data.get('address_id', instance.address_id)
        instance.save()
        return instance

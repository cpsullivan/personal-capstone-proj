from rest_framework import serializers
from .models import CorrespondentAddress


class CorrespondentAddressSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    street_number = serializers.CharField(max_length=10)
    street_name = serializers.CharField(max_length=50)
    city = serializers.CharField(max_length=50)
    country = serializers.CharField(max_length=20)
    postal_code = serializers.CharField(max_length=12)

    def create(self, validated_data):
        return CorrespondentAddress.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.id = validated_data.get('id', instance.id)
        instance.street_number = validated_data.get('street_number', instance.street_number)
        instance.street_name = validated_data.get('street_name', instance.street_name)
        instance.city = validated_data.get('city', instance.city)
        instance.country = validated_data.get('country', instance.country)
        instance.postal_code = validated_data.get('postal_code', instance.postal_code)
        instance.save()
        return instance

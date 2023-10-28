from rest_framework import serializers
from .models import ArtsUser


class ArtsUserSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    user_last_name = serializers.CharField(max_length=50)
    user_first_name = serializers.CharField(max_length=50)
    user_org_element = serializers.IntegerField()
    user_type = serializers.CharField()

    def create(self, validated_data):
        return ArtsUser.objects.create(**validated_data)


    def update(self, instance, validated_data):
        instance.id = validated_data.get('id', instance.id)
        instance.user_last_name = validated_data.get('user_last_name', instance.user_last_name)
        instance.user_first_name = validated_data.get('user_first_name', instance.user_first_name)
        instance.user_org_element = validated_data.get('user_org_element', instance.user_org_element)
        instance.user_type = validated_data.get('user_type', instance.user_type)
        instance.save()
        return instance

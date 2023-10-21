from rest_framework import serializers
from .models import Correspondence


class CorrespondenceSerializer(serializers.Serializer):
    correspondence_type = serializers.CharField(read_only=True)
    correspondence_date = serializers.DateTimeField(read_only=True)
    id = serializers.IntegerField(read_only=True)
    correspondence_document = serializers.FileField()
    

    def create(self, validated_data):
        return Correspondence.objects.create(**validated_data)


    def update(self, instance, validated_data):
        instance.correspondence_type = validated_data.get('correspondence_type', instance.correspondence_type)
        instance.action = validated_data.get('action', instance.action)
        instance.id = validated_data.get('id', instance.id)
        instance.correspondence_document = validated_data.get('correspondence_document', instance.correspondence_document)
        instance.save()
        return instance

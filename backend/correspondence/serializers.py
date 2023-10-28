from rest_framework import serializers
from .models import Correspondence


class CorrespondenceSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    correspondence_type = serializers.CharField(max_length=3)
    correspondence_date = serializers.DateTimeField()
    correspondence_document = serializers.FileField()
    

    def create(self, validated_data):
        return Correspondence.objects.create(**validated_data)


    def update(self, instance, validated_data):
        instance.id = validated_data.get('id', instance.id)
        instance.correspondence_type = validated_data.get('correspondence_type', instance.correspondence_type)
        instance.correspondence_date = validated_data.get('correspondence_date', instance.correspondence_date)
        instance.correspondence_document = validated_data.get('correspondence_document', instance.correspondence_document)
        instance.save()
        return instance

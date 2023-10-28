from rest_framework import serializers
from .models import ResponseDocument


class ResponseDocumentSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    action_request_id = serializers.IntegerField()
    template_id = serializers.IntegerField()
    response_document = serializers.FileField()

    def create(self, validated_data):
        return ResponseDocument.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.id = validated_data.get('id', instance.id)
        instance.template_id = validated_data.get('template_id', instance.template_id)
        instance.response_document = validated_data.get('response_document', instance.response_document)
        instance.save()
        return instance

from rest_framework import serializers
from .models import Templates


class TemplateSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    template_type = serializers.CharField(max_length=50)
    template_use = serializers.CharField(max_length=255)
    template_document = serializers.FileField()

    def create(self, validated_data):
        return Templates.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.id = validated_data.get('id', instance.id)
        instance.template_type = validated_data.get('template_type', instance.template_type)
        instance.template_use = validated_data.get('template_use', instance.template_use)
        instance.template_document = validated_data.get('template_document', instance.template_document)
        instance.save()
        return instance

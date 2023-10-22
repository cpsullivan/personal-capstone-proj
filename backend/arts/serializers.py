from rest_framework import serializers
from .models import ActionRequest


class ActionRequestSerializer(serializers.Serializer):
    action_request_title = serializers.CharField(max_length=255)
    created_on = serializers.DateTimeField(read_only=True)
    action = serializers.CharField()
    due_date = serializers.DateTimeField(read_only=True)
    comments = serializers.CharField()
    id = serializers.IntegerField(read_only=True)
    documents = serializers.FileField()
    

    def create(self, validated_data):
        return ActionRequest.objects.create(**validated_data)


    def update(self, instance, validated_data):
        instance.action_request_title = validated_data.get('action_request_title', instance.action_request_title)
        instance.action = validated_data.get('action', instance.action)
        instance.comments = validated_data.get('comments', instance.comments)
        instance.id = validated_data.get('id', instance.id)
        instance.documents = validated_data.get('documents', instance.documents)
        instance.save()
        return instance

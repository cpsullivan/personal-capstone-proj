from rest_framework import serializers
#from django.utils import timezone
#from datetime import date
from .models import ActionRequest


class ActionRequestSerializer(serializers.Serializer):
    #class Meta:
    #   model = ActionRequest
    #   fields = '__all__'
    #   date_format = '%Y-%m-%d'
    
    id = serializers.IntegerField(read_only=True)
    action_request_title = serializers.CharField(max_length=255)
    created_on = serializers.DateTimeField()
    correspondent_id = serializers.IntegerField()
    action = serializers.CharField()
    due_date = serializers.DateTimeField()
    comments = serializers.CharField()
    documents = serializers.IntegerField()

    def create(self, validated_data):
        return ActionRequest.objects.create(**validated_data)


    def update(self, instance, validated_data):
        instance.id = validated_data.get('id', instance.id)
        instance.action_request_title = validated_data.get('action_request_title', instance.action_request_title)
        instance.created_on = validated_data.get('created_on', instance.created_on)
        instance.correspondent_id = validated_data.get('correspondent_id', instance.correspondent_id)
        instance.action = validated_data.get('action', instance.action)
        instance.due_date = validated_data.get('due_date', instance.due_date)
        instance.comments = validated_data.get('comments', instance.comments)
        instance.documents = validated_data.get('documents', instance.documents)
        instance.save()
        return instance

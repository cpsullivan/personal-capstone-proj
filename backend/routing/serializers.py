from rest_framework import serializers
from .models import Routing


class RoutingSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    action_request_id = serializers.IntegerField()
    routing_from = serializers.IntegerField()
    routing_to = serializers.IntegerField()
    date_routed = serializers.DateTimeField()
    routing_reason = serializers.CharField(max_value=255)
    action_requested = serializers.CharField(max_value=255)

    def create(self, validated_data):
        return Routing.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.id = validated_data.get('id', instance.id)
        instance.action_request_id = validated_data.get('action_request_id', instance.action_request_id)
        instance.routing_from = validated_data.get('routing_from', instance.routing_from)
        instance.routing_to = validated_data.get('routing_to', instance.routing_to)
        instance.date_routed = validated_data.get('date_routed', instance.date_routed)
        instance.routing_reason = validated_data.get('routing_reason', instance.routing_reason)
        instance.action_requested = validated_data.get('action_requested', instance.action_requested)
        instance.save()
        return instance

from rest_framework import serializers
from .models import OrganizationElement


class OrganizationElementSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    org_element_name = serializers.CharField(max_length=50)

    def create(self, validated_data):
        return OrganizationElement.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.id = validated_data.get('id', instance.id)
        instance.org_element_name = validated_data.get('org_element_name', instance.org_element_name)
        instance.save()
        return instance

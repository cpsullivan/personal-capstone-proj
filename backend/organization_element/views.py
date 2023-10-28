from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from .serializers import OrganizationElementSerializer
from .models import OrganizationElement


class OrganizationElementView(APIView):

    def get(self, request, pk=None):
        if pk:  
            data = OrganizationElement.objects.get(pk=pk)
            serializer = OrganizationElementSerializer(data)
        else:
            data = OrganizationElement.objects.all()
            serializer = OrganizationElementSerializer(data, many=True)
        return Response({"result": serializer.data})

    def post(self, request):
        organization_element = request.data
        serializer = OrganizationElementSerializer(data=organization_element)
        if serializer.is_valid(raise_exception=True):
            organization_element_saved = serializer.save()
        return Response({"result": f"{organization_element_saved.id} saved"})

    def put(self, request, pk):
        saved_organization_element = get_object_or_404(OrganizationElement.objects.all(), pk=pk)
        data = request.data
        serializer = OrganizationElementSerializer(instance=saved_organization_element, data=data, partial=True)
        if serializer.is_valid(raise_exception=True):
            saved_organization_element = serializer.save()
        return Response({"result": f"{saved_organization_element.id} updated"})

    def delete(self, request, pk):
        organization_element = get_object_or_404(OrganizationElement.objects.all(), pk=pk)
        organization_element.delete()
        return Response({"result": f"Organization element id {pk} deleted"},status=204)

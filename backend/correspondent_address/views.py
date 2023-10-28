from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from .serializers import CorrespondentAddressSerializer
from .models import CorrespondentAddress


class CorrespondentAddressView(APIView):

    def get(self, request, pk=None):
        if pk:  
            data = CorrespondentAddress.objects.get(pk=pk)
            serializer = CorrespondentAddressSerializer(data)
        else:
            data = CorrespondentAddress.objects.all()
            serializer = CorrespondentAddressSerializer(data, many=True)
        return Response({"result": serializer.data})

    def post(self, request):
        correspondent_address = request.data
        serializer = CorrespondentAddressSerializer(data=correspondent_address)
        if serializer.is_valid(raise_exception=True):
            correspondent_address_saved = serializer.save()
        return Response({"result": f"{correspondent_address_saved.id} saved"})

    def put(self, request, pk):
        saved_correspondent_address = get_object_or_404(CorrespondentAddress.objects.all(), pk=pk)
        data = request.data
        serializer = CorrespondentAddressSerializer(instance=saved_correspondent_address, data=data, partial=True)
        if serializer.is_valid(raise_exception=True):
            saved_correspondent_address = serializer.save()
        return Response({"result": f"{saved_correspondent_address.id} updated"})

    def delete(self, request, pk):
        correspondent_address = get_object_or_404(CorrespondentAddress.objects.all(), pk=pk)
        correspondent_address.delete()
        return Response({"result": f"Correspondent address id {pk} deleted"},status=204)

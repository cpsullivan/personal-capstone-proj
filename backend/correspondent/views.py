from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from .serializers import CorrespondentSerializer
from .models import Correspondent


class CorrespondentView(APIView):

    def get(self, request, pk=None):
        if pk:  
            data = Correspondent.objects.get(pk=pk)
            serializer = CorrespondentSerializer(data)
        else:
            data = Correspondent.objects.all()
            serializer = CorrespondentSerializer(data, many=True)
        return Response({"result": serializer.data})

    def post(self, request):
        Correspondent = request.data
        serializer = CorrespondentSerializer(data=Correspondent)
        if serializer.is_valid(raise_exception=True):
            Correspondent_saved = serializer.save()
        return Response({"result": f"{Correspondent_saved.id} saved"})

    def put(self, request, pk):
        saved_Correspondent = get_object_or_404(Correspondent.objects.all(), pk=pk)
        data = request.data
        serializer = CorrespondentSerializer(instance=saved_Correspondent, data=data, partial=True)
        if serializer.is_valid(raise_exception=True):
            saved_Correspondent = serializer.save()
        return Response({"result": f"{saved_Correspondent.id} updated"})

    def delete(self, request, pk):
        Correspondent = get_object_or_404(Correspondent.objects.all(), pk=pk)
        Correspondent.delete()
        return Response({"result": f"Correspondent id {pk} deleted"},status=204)

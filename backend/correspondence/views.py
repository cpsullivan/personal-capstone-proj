from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from .serializers import CorrespondenceSerializer
from .models import Correspondence


class CorrespondenceView(APIView):

    def get(self, request, pk=None):
        if pk:  
            data = Correspondence.objects.get(pk=pk)
            serializer = CorrespondenceSerializer(data)
        else:
            data = Correspondence.objects.all()
            serializer = CorrespondenceSerializer(data, many=True)
        return Response({"result": serializer.data})

    def post(self, request):
        correspondence = request.data
        serializer = CorrespondenceSerializer(data=correspondence)
        if serializer.is_valid(raise_exception=True):
            correspondence_saved = serializer.save()
        return Response({"result": f"{correspondence_saved.correspondence_type} of {correspondence_saved.correspondence_date} saved"})

    def put(self, request, pk):
        saved_correspondence = get_object_or_404(Correspondence.objects.all(), pk=pk)
        data = request.data
        serializer = CorrespondenceSerializer(instance=saved_correspondence, data=data, partial=True)
        if serializer.is_valid(raise_exception=True):
            saved_correspondence = serializer.save()
        return Response({"result": f"{saved_correspondence.correspondence_type} of {saved_correspondence.correspondence_date} updated"})

    def delete(self, request, pk):
        correspondence = get_object_or_404(Correspondence.objects.all(), pk=pk)
        correspondence.delete()
        return Response({"result": f"Correspondence id {pk} deleted"},status=204)

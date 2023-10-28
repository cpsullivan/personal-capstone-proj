from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from .serializers import ResponseDocumentSerializer
from .models import ResponseDocument


class ResponseDocumentView(APIView):

    def get(self, request, pk=None):
        if pk:  
            data = ResponseDocument.objects.get(pk=pk)
            serializer = ResponseDocumentSerializer(data)
        else:
            data = ResponseDocument.objects.all()
            serializer = ResponseDocumentSerializer(data, many=True)
        return Response({"result": serializer.data})

    def post(self, request):
        response_document = request.data
        serializer = ResponseDocumentSerializer(data=response_document)
        if serializer.is_valid(raise_exception=True):
            response_document_saved = serializer.save()
        return Response({"result": f"{response_document_saved.id} saved"})

    def put(self, request, pk):
        saved_response_document = get_object_or_404(ResponseDocument.objects.all(), pk=pk)
        data = request.data
        serializer = ResponseDocumentSerializer(instance=saved_response_document, data=data, partial=True)
        if serializer.is_valid(raise_exception=True):
            saved_response_document = serializer.save()
        return Response({"result": f"{saved_response_document.id} updated"})

    def delete(self, request, pk):
        response_document = get_object_or_404(ResponseDocument.objects.all(), pk=pk)
        response_document.delete()
        return Response({"result": f"Response document id {pk} deleted"},status=204)

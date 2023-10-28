from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from .serializers import TemplateSerializer
from .models import Templates


class TemplateView(APIView):

    def get(self, request, pk=None):
        if pk:  
            data = Templates.objects.get(pk=pk)
            serializer = TemplateSerializer(data)
        else:
            data = Templates.objects.all()
            serializer = TemplateSerializer(data, many=True)
        return Response({"result": serializer.data})

    def post(self, request):
        template = request.data
        serializer = TemplateSerializer(data=template)
        if serializer.is_valid(raise_exception=True):
            template_saved = serializer.save()
        return Response({"result": f"{template_saved.id} saved"})

    def put(self, request, pk):
        saved_template = get_object_or_404(Templates.objects.all(), pk=pk)
        data = request.data
        serializer = TemplateSerializer(instance=saved_template, data=data, partial=True)
        if serializer.is_valid(raise_exception=True):
            saved_template = serializer.save()
        return Response({"result": f"{saved_template.id} updated"})

    def delete(self, request, pk):
        template = get_object_or_404(Templates.objects.all(), pk=pk)
        template.delete()
        return Response({"result": f"Template id {pk} deleted"},status=204)

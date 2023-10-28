from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from .serializers import ArtsUserSerializer
from .models import ArtsUser


class ArtsUserView(APIView):
    def get(self, request, pk=None):
        if pk:  
            data = ArtsUser.objects.get(pk=pk)
            serializer = ArtsUserSerializer(data)
        else:
            data = ArtsUser.objects.all()
            serializer = ArtsUserSerializer(data, many=True)
        return Response({"result": serializer.data})

    def post(self, request):
        arts_user = request.data
        serializer = ArtsUserSerializer(data=arts_user)
        if serializer.is_valid(raise_exception=True):
            arts_user_saved = serializer.save()
        return Response({"result": f"{arts_user_saved.id} saved"})

    def put(self, request, pk):
        saved_arts_user = get_object_or_404(ArtsUser.objects.all(), pk=pk)
        data = request.data
        serializer = ArtsUserSerializer(instance=saved_arts_user, data=data, partial=True)
        if serializer.is_valid(raise_exception=True):
            saved_arts_user = serializer.save()
        return Response({"result": f"{saved_arts_user.id} updated"})

    def delete(self, request, pk):
        arts_user = get_object_or_404(ArtsUser.objects.all(), pk=pk)
        arts_user.delete()
        return Response({"result": f"ARTS user id {pk} deleted"},status=204)

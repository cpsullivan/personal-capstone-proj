from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from .serializers import RoutingSerializer
from .models import Routing


class RoutingView(APIView):

    def get(self, request, pk=None):
        if pk:  
            data = Routing.objects.get(pk=pk)
            serializer = RoutingSerializer(data)
        else:
            data = Routing.objects.all()
            serializer = RoutingSerializer(data, many=True)
        return Response({"result": serializer.data})

    def post(self, request):
        routing = request.data
        serializer = RoutingSerializer(data=routing)
        if serializer.is_valid(raise_exception=True):
            routing_saved = serializer.save()
        return Response({"result": f"{routing_saved.id} saved"})

    def put(self, request, pk):
        saved_routing = get_object_or_404(Routing.objects.all(), pk=pk)
        data = request.data
        serializer = RoutingSerializer(instance=saved_routing, data=data, partial=True)
        if serializer.is_valid(raise_exception=True):
            saved_routing = serializer.save()
        return Response({"result": f"{saved_routing.id} updated"})

    def delete(self, request, pk):
        routing = get_object_or_404(Routing.objects.all(), pk=pk)
        routing.delete()
        return Response({"result": f"Routing id {pk} deleted"},status=204)

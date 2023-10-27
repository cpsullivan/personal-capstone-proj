from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from .serializers import ActionRequestSerializer
from .models import ActionRequest #, add_business_days
#from django.http import JsonResponse
#from django.utils import timezone


class ActionRequestView(APIView):

    #def get_due_date(request):
    #    due_date = add_business_days(timezone.now(), 10)
    #    return JsonResponse({'due_date': due_date})

    def get(self, request, pk=None):
        if pk:  
            data = ActionRequest.objects.get(pk=pk)
            serializer = ActionRequestSerializer(data)
        else:
            data = ActionRequest.objects.all()
            serializer = ActionRequestSerializer(data, many=True)
        return Response({"result": serializer.data})

    def post(self, request):
        action_request = request.data
        serializer = ActionRequestSerializer(data=action_request)
        if serializer.is_valid(raise_exception=True):
            action_request_saved = serializer.save()
        return Response({"result": f"{action_request_saved.action_request_title} saved"})

    def put(self, request, pk):
        saved_action_request = get_object_or_404(ActionRequest.objects.all(), pk=pk)
        data = request.data
        serializer = ActionRequestSerializer(instance=saved_action_request, data=data, partial=True)
        if serializer.is_valid(raise_exception=True):
            saved_action_request = serializer.save()
        return Response({"result": f"{saved_action_request.action_request_title} updated"})

    def delete(self, request, pk):
        action_request = get_object_or_404(ActionRequest.objects.all(), pk=pk)
        action_request.delete()
        return Response({"result": f"Action Request id {pk} deleted"},status=204)

from django.db import models
from datetime import datetime
from arts.models import ActionRequest
from organization_element.models import OrganizationElement

# Create your models here.

class Routing(models.Model):
    action_request_id = models.ForeignKey(ActionRequest, on_delete=models.CASCADE)
    routing_from = models.ForeignKey(OrganizationElement, on_delete=models.CASCADE)
    routing_to = models.ForeignKey(OrganizationElement, on_delete=models.CASCADE)
    date_routed = models.DateTimeField(default=datetime.now())
    routing_reason = models.CharField(max_length=255)
    action_requested = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.id
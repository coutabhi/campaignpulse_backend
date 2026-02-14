from rest_framework.viewsets import ModelViewSet
from rest_framework.exceptions import PermissionDenied
from .models import Campaign
from .serializers import CampaignSerializer
from .pagination import CampaignCursorPagination

class CampaignViewSet(ModelViewSet):

    queryset = Campaign.objects.all().order_by('-created_at')
    serializer_class = CampaignSerializer
    pagination_class = CampaignCursorPagination

    def perform_destroy(self, instance):
        if instance.status != "Draft":
            raise PermissionDenied("Only Draft campaigns can be deleted")
        instance.delete()

    def perform_update(self, serializer):
        instance = serializer.instance
        if instance.status == "Completed":
            raise PermissionDenied("Completed campaigns cannot be edited")
        serializer.save()

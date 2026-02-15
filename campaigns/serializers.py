# campaigns/serializers.py
from rest_framework import serializers
from .models import Campaign

class CampaignSerializer(serializers.ModelSerializer):
    class Meta:
        model = Campaign
        fields = "__all__"
        read_only_fields = ["id", "created_at", "updated_at", "likes", "comments"]

    def validate(self, data):
        instance = getattr(self, "instance", None)

        start = data.get("start_date", instance.start_date if instance else None)
        end = data.get("end_date", instance.end_date if instance else None)

        if start and end and end < start:
            raise serializers.ValidationError("end_date cannot be before start_date")

        budget = data.get("budget", instance.budget if instance else None)
        if budget is not None and budget <= 0:
            raise serializers.ValidationError("budget must be greater than 0")

        return data
from rest_framework import serializers
from .models import Campaign

class CampaignSerializer(serializers.ModelSerializer):

    class Meta:
        model = Campaign
        fields = "__all__"
        read_only_fields = ["likes", "comments"]

    def validate(self, data):
        if data["end_date"] < data["start_date"]:
            raise serializers.ValidationError("end_date cannot be before start_date")

        if data["budget"] <= 0:
            raise serializers.ValidationError("budget must be greater than 0")

        return data
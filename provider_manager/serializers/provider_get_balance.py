from rest_framework import serializers
from provider_manager.models.provider import Provider


# Serialize python obj or dicts into JSON


class ProviderGetBalanceSerializer(serializers.Serializer):
    token = serializers.CharField()
    account = serializers.CharField()

    class Meta:
        extra_kwargs = {
            "token": {"error_messages": {
                "blank": "This is a required param"
            }},
            "account": {"error_messages": {
                "blank": "This is a required param"
            }}
        }

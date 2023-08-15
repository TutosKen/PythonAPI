from rest_framework import serializers
from authentication.models import Merchant

# Serialize python obj or dicts into JSON


class MerchantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Merchant
        fields = ('login', 'password', 'active',)
        read_only_fields = ('id',)
        extra_kwargs = {
            "password": {"error_messages": {
                "blank": "This is a required param"
            }},
            "login": {"error_messages": {
                "blank": "This is a required param"
            }}
        }

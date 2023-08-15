from rest_framework.decorators import api_view
from myproject.api import error_codes
from myproject.api.custom_response import CustomResponse
from authentication.models.merchant_token import MerchantToken
from .serializers import *
from rest_framework.exceptions import ValidationError
from django.core.exceptions import ObjectDoesNotExist
from .providers.banking.example import Example

# Global instances for this file
res = CustomResponse()


# Get customer account balance
@api_view(['POST'])
def get_balance(request):
    serializer = ProviderGetBalanceSerializer(data=request.data)

    try:
        if serializer.is_valid(raise_exception=True):
            merchant_token = MerchantToken.objects.get(
                token=serializer.validated_data["token"])

            valid_token = merchant_token.check_token()
            if valid_token:
                provider = Example()
                account = serializer.validated_data["account"]
                balance = provider.get_balance(account)

                res.add_update_response_attr("balance", balance)
                return res.success_response()
    except ValidationError:
        return res.error_response(error_codes.INVALID_PARAMETER, serializer.errors)
    except ObjectDoesNotExist:
        return res.error_response(error_codes.OBJECT_NOT_FOUND, "Please login first!")

    return res.error_response(error_codes.GENERAL_ERR, "You are not worthy!")

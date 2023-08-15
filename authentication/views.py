from rest_framework.decorators import api_view
from myproject.api import error_codes
from myproject.api.custom_response import CustomResponse
from .models import *
from .serializers import *
from rest_framework.serializers import ValidationError
from django.core.exceptions import ObjectDoesNotExist
from myproject.util.encoding import Encoding

# Global instances for this file
res = CustomResponse()

# Validate credentials and generate an auth token


@api_view(['POST'])
def validate_credentials(request):
    serializer = MerchantSerializer(data=request.data)

    try:
        if serializer.is_valid(raise_exception=True):

            usr = serializer.validated_data["login"]
            pwd = serializer.validated_data["password"]

            match_merchant = Merchant.objects.get(login=usr)

            encoder = Encoding()
            if encoder.argon2_verify(pwd, match_merchant.password):
                new_token = encoder.generate_auth_token()

            try:
                merchant_token = MerchantToken.objects.get(
                    merchant_id=match_merchant.id)
            except ObjectDoesNotExist:
                merchant_token = None

                if merchant_token is not None:
                    merchant_token.token = new_token
                    merchant_token.save()
                else:
                    MerchantToken.objects.create(
                        merchant_id=match_merchant.id, token=new_token, expiration_time=10)

                res.add_update_response_attr(
                    "token", new_token)
                return res.success_response()
            else:
                return res.error_response(error_codes.INVALID_CREDS, "Invalid credentials, bad boy >:c")
    except ValidationError:
        return res.error_response(error_codes.INVALID_PARAMETER, serializer.errors)
    except ObjectDoesNotExist:
        return res.error_response(error_codes.OBJECT_NOT_FOUND, "User {usr} not found")

    return res.error_response(error_codes.GENERAL_ERR, "Well, this is embarrassing...")


# Dummy function to see how response works
@api_view(['POST'])
def dummyEndpoint(request):
    res.add_update_response_attr(
        "message", "Yeap, you guessed it, it's just a dumb endpoint")
    return res.success_response()

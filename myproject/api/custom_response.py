from rest_framework.response import Response
from rest_framework import status


class CustomResponse():

    response_attributes = {}

    def __init__(self):
        self.add_update_response_attr("success", True)
        self.add_update_response_attr("error_code", 0)

    # Add or update custom key/value pairs to response
    def add_update_response_attr(self, key: str, value: any):
        self.response_attributes[key] = value

    # Successfull response
    def success_response(self, status_code=status.HTTP_200_OK):
        return Response(self.response_attributes, status_code)

    # Error response
    def error_response(self, error_code: int, message: str, status_code=status.HTTP_400_BAD_REQUEST):
        self.add_update_response_attr("success", False)
        self.add_update_response_attr("error_code", error_code)
        self.add_update_response_attr("message", message)

        return Response(self.response_attributes, status_code)

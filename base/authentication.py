from rest_framework.authentication import TokenAuthentication
from drf_spectacular.extensions import OpenApiAuthenticationExtension

HEADER_NAME = "X-API-KEY"


class XApiKeyTokenAuthentication(TokenAuthentication):
    header = HEADER_NAME

    def authenticate(self, request):
        token = request.META.get(f'HTTP_{self.header.upper().replace("-", "_")}')
        return self.authenticate_credentials(token) if token else None


class XApiKeyTokenScheme(OpenApiAuthenticationExtension):
    """
    OpenAPI documentation for the custom token authentication.
    """

    target_class = "base.authentication.XApiKeyTokenAuthentication"
    name = HEADER_NAME

    def get_security_definition(self, auto_schema):
        return {
            "type": "apiKey",
            "in": "header",
            "name": HEADER_NAME,
            "description": f"Token-based authentication with {HEADER_NAME} header",
        }

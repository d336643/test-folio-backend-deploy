from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.exceptions import InvalidToken


class JWTAuthenticationSafe(JWTAuthentication):
    def authenticate(self, request):
        try:
            return super().authenticate(request=request)
        except InvalidToken:
            return None


# def enforce_csrf(request):
#     check = CSRFCheck()
#     check.process_request(request)
#     reason = check.process_view(request, None, (), {})
#     if reason:
#         raise exceptions.PermissionDenied("CSRF Failed: %s" % reason)


# class CustomAuthentication(JWTAuthentication):
#     """Use this functino when tokens are saved in cookie"""

#     def authenticate(self, request):
#         header = self.get_header(request)
#         if header is None:  # try to get access token
#             raw_token = request.COOKIES.get(settings.SIMPLE_JWT["AUTH_COOKIE"]) or None
#         else:
#             raw_token = self.get_raw_token(header)

#         if raw_token is None:
#             return None

#         validated_token = self.get_validated_token(raw_token)

#         enforce_csrf(request)
#         return self.get_user(validated_token), validated_token

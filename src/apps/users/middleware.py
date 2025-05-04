from django.http import JsonResponse
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.exceptions import AuthenticationFailed

class RoleRequiredMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        self.jwt_authenticator = JWTAuthentication()

    def __call__(self, request):
        if request.path.startswith('/api/admin/'):  # Пример защищённого маршрута
            try:
                user_auth_tuple = self.jwt_authenticator.authenticate(request)
                if user_auth_tuple is None:
                    raise AuthenticationFailed("Требуется авторизация")

                user, _ = user_auth_tuple

                if user.role != 'admin':
                    return JsonResponse({'detail': 'Доступ только для администраторов'}, status=403)
            except AuthenticationFailed as e:
                return JsonResponse({'detail': str(e)}, status=401)

        return self.get_response(request)

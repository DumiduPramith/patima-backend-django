from django.http import JsonResponse
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from patima.utils.custom_jwt_authentication import CustomJWTAuthentication


class CheckAuthentication(APIView):
    authentication_classes = [CustomJWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return JsonResponse({'message': 'User is authenticated.'})

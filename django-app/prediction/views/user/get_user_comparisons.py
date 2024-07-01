from rest_framework.views import APIView
from django.http.response import JsonResponse
import json

from prediction.utils.prediction_handler import PredictionHandler

from patima.utils.custom_jwt_authentication import CustomJWTAuthentication
from rest_framework.permissions import IsAuthenticated
from patima.permission.is_archeo_general import IsArcheoLogistOrGeneralPub

class GetUserComparisons(APIView):
    authentication_classes = [CustomJWTAuthentication]
    permission_classes = [IsAuthenticated, IsArcheoLogistOrGeneralPub]

    def get(self, request):
        user_obj = request.user
        prediction_handler = PredictionHandler(user_obj)
        try:
            page_number = json.loads(request.body.decode('utf-8')).get('page')
        except AttributeError:
            return JsonResponse({'status': 'error', 'message': 'Page number is required'}, status=400)
        except json.JSONDecodeError:
            return JsonResponse({'status': 'error', 'message': 'Invalid JSON format'}, status=400)
        predictions = prediction_handler.retrieve_predictions_by_user_id(page_number)
        if predictions is False:
            return JsonResponse({'status': 'error', 'message': 'Internal server error'}, status=404)
        return JsonResponse({'status': 'success', 'predictions': predictions}, status=200)

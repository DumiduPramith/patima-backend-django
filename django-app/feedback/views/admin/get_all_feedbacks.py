from rest_framework.views import APIView
from django.http import JsonResponse
import json

from patima.utils.custom_jwt_authentication import CustomJWTAuthentication
from rest_framework.permissions import IsAuthenticated
from patima.permission.is_admin import IsAdmin

from feedback.utils.feedback_handler import FeedbackHandler

class GetAllFeedbacks(APIView):
    authentication_classes = [CustomJWTAuthentication]
    permission_classes = [IsAuthenticated, IsAdmin]

    def get(self, request, *args, **kwargs):
        user = request.user
        try:
            page_number = int(request.GET.get('page_number', 1))
        except Exception as e:
            return JsonResponse({"status":"error",'message': 'Invalid page number'}, status=400)
        feedback_handler = FeedbackHandler(user)
        feedbacks = feedback_handler.get_all_feedbacks(page_number)
        if not feedbacks:
            return JsonResponse({"status":"error",'message': 'Error occurred while getting feedbacks'}, status=500)
        return JsonResponse({'status' : 'success' ,'feedbacks': feedbacks})

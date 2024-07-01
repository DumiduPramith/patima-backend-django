from rest_framework.views import APIView
from django.http import JsonResponse
import json

from patima.utils.custom_jwt_authentication import CustomJWTAuthentication
from rest_framework.permissions import IsAuthenticated
from patima.permission.is_admin import IsAdmin

from admin_messages.models.message import Message

class MarkAsRead(APIView):
    # mark message as read
    authentication_classes = [CustomJWTAuthentication]
    permission_classes = [IsAuthenticated, IsAdmin]

    def put(self, request):
        try:
            data = json.loads(request.body.decode('utf-8'))
            message_id = data['message_id']
        except json.JSONDecodeError:
            return JsonResponse({'status': 'error', 'message': 'Invalid JSON'}, status=400)
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': 'internal server error'}, status=500)
        message_obj = Message()
        status = message_obj.mark_as_read(message_id)
        if status:
            return JsonResponse({'status': 'success', 'message': 'Message marked as read'})
        else:
            return JsonResponse({'status': 'error', 'message': 'Message mark as read failed'}, status=500)

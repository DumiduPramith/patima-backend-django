import json

from django.http import JsonResponse
from rest_framework.views import APIView
from django.apps import apps

from patima.permission.is_admin import IsAdmin


class ChangeSegmentationModel(APIView):
    # change segmentation model
    permission_classes = [IsAdmin]

    def put(self, request, *args, **kwargs):
        try:
            data = json.loads(request.body.decode('utf-8'))
            segmentation_model = data['segmentation_model']
        except json.JSONDecodeError:
            return JsonResponse({'status': 'error', 'message': 'Invalid JSON'}, status=400)
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': 'internal server error'}, status=500)
        if segmentation_model == 'yolo':
            apps.get_app_config('prediction').chosen_segmentation_model = 'yolo'
        elif segmentation_model == 'unet':
            apps.get_app_config('prediction').chosen_segmentation_model = 'unet'
        else:
            return JsonResponse({'status': 'error', 'message': 'Invalid segmentation model'}, status=400)
        return JsonResponse({'status': 'success', 'message': 'Segmentation model changed successfully'})

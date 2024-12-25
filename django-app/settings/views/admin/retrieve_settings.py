from django.http import JsonResponse
from rest_framework.views import APIView
from django.apps import apps

from patima.permission.is_admin import IsAdmin


class RetrieveSettingsView(APIView):
    permission_classes = [IsAdmin]

    def get(self, request, *args, **kwargs):
        selected_segmentation_model = apps.get_app_config('prediction').chosen_segmentation_model
        if selected_segmentation_model is None:
            return JsonResponse({'status': 'error', 'message': 'Segmentation model not selected'}, status=400)
        return JsonResponse({'status': 'success', 'settings': [{
            'title' : 'Segmentation Model',
            'selections' : {
                'selected' : selected_segmentation_model,
                'options' : ['yolo', 'unet']
            }
        }]}, status=200)

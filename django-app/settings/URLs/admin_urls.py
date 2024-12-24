from django.urls import path

from settings.views.admin.change_segmentation_model import ChangeSegmentationModel

urlpatterns = [
    path('change-segmentation-model',ChangeSegmentationModel.as_view(),name='change_segmentation_model'),
 ]
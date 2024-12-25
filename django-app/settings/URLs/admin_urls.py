from django.urls import path

from settings.views.admin.change_segmentation_model import ChangeSegmentationModel
from settings.views.admin.retrieve_settings import RetrieveSettingsView

urlpatterns = [
    path('change-segmentation-model',ChangeSegmentationModel.as_view(),name='change_segmentation_model'),
    path('retrieve',RetrieveSettingsView.as_view(),name='retrieve_settings'),
 ]

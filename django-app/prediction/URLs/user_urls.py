from django.urls import path

from prediction.views.user.get_nearby_predictions import GetNearbyPredictions
from prediction.views.user.get_user_comparisons import GetUserComparisons
from prediction.views.user.retrieve_user_predictions import RetrieveUserPredictions

urlpatterns = [
    path('retrieve-predictions', RetrieveUserPredictions.as_view(), name='retrieve_user_predictions'),
    path('retrieve-comparisons', GetUserComparisons.as_view(), name='get_user_comparisons'),
    path('get-nearby-predictions',GetNearbyPredictions.as_view(),name='get_nearby_predictions'),
]

from django.urls import path,include
from prediction.views.user.new_predict import Predict


urlpatterns = [
    path('new', Predict.as_view(), name="new_predict"),
    path('admin/', include('prediction.URLs.admin_urls')),
    path('user/', include('prediction.URLs.user_urls')),
]

from django.urls import include,path

urlpatterns = [
    path('admin/',include('settings.URLs.admin_urls') ),
]
from django.urls import path
from zip_file import views

urlpatterns = [
    path('upload-zip/', views.upload_zip, name='upload-zip' ),
]

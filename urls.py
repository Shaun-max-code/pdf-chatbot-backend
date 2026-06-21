from django.urls import path
from .views import PDFUploadView
from django.urls import path, include

urlpatterns = [
    path('upload/', PDFUploadView.as_view()),
]
urlpatterns = [
    path('api/', include('chatbot.urls')),
]
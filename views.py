from rest_framework.generics import CreateAPIView
from .models import PDFDocument
from .serializers import PDFDocumentSerializer

class PDFUploadView(CreateAPIView):
    queryset = PDFDocument.objects.all()
    serializer_class = PDFDocumentSerializer
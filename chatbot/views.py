from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import PDFDocument
from .serializers import PDFDocumentSerializer
from .pdf_utils import extract_text_from_pdf


class PDFUploadView(APIView):

    def post(self, request):
        serializer = PDFDocumentSerializer(data=request.data)

        if serializer.is_valid():
            pdf = serializer.save()

            pdf_text = extract_text_from_pdf(pdf.pdf_file.path)

            print("\n" + "=" * 60)
            print("PDF TEXT")
            print("=" * 60)
            print(pdf_text[:1000])   # Print first 1000 characters
            print("=" * 60 + "\n")

            return Response(
                {
                    "message": "PDF uploaded successfully",
                    "characters": len(pdf_text),
                },
                status=status.HTTP_201_CREATED,
            )

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
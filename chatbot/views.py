from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import PDFDocument, DocumentChunk
from .serializers import PDFDocumentSerializer
from .services.pdf_service import PDFService
from .services.chunk_service import ChunkService


class PDFUploadView(APIView):

    def post(self, request):
        serializer = PDFDocumentSerializer(data=request.data)

        if serializer.is_valid():
            pdf = serializer.save()

            # Extract text from PDF
            pdf_text = PDFService.extract_text(pdf.pdf_file.path)

            # Split into chunks
            chunks = ChunkService.split_into_chunks(pdf_text)

            # Save chunks to database
            for index, chunk in enumerate(chunks):
                DocumentChunk.objects.create(
                    document=pdf,
                    chunk_index=index,
                    text=chunk,
                )

            print("\n" + "=" * 60)
            print("PDF TEXT")
            print("=" * 60)
            print(pdf_text[:1000])
            print("=" * 60 + "\n")

            return Response(
                {
                    "message": "PDF uploaded successfully",
                    "characters": len(pdf_text),
                    "chunks": len(chunks),
                },
                status=status.HTTP_201_CREATED,
            )

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
from django.db import models


class PDFDocument(models.Model):
    title = models.CharField(max_length=255)
    pdf_file = models.FileField(upload_to="pdfs/")
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class DocumentChunk(models.Model):
    document = models.ForeignKey(
        PDFDocument,
        on_delete=models.CASCADE,
        related_name="chunks",
    )

    chunk_index = models.IntegerField()

    text = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.document.title} - Chunk {self.chunk_index}"
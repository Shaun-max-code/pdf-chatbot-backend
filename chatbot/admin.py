from django.contrib import admin
from .models import PDFDocument, DocumentChunk

admin.site.register(PDFDocument)
admin.site.register(DocumentChunk)
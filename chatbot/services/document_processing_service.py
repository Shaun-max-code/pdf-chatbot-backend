from .pdf_service import PDFService
from .chunk_service import ChunkService
from .embedding_service import EmbeddingService
from .vector_store import VectorStore

from chatbot.models import DocumentChunk


class DocumentProcessingService:

    @staticmethod
    def process(document):

        # Extract text
        text = PDFService.extract_text(document.pdf_file.path)

        # Chunk text
        chunks = ChunkService.split_into_chunks(text)

        # Process each chunk
        for index, chunk in enumerate(chunks):

            db_chunk = DocumentChunk.objects.create(
                document=document,
                chunk_index=index,
                text=chunk,
            )

            embedding = EmbeddingService.generate_embedding(chunk)

            VectorStore.add_chunk(
                chunk_id=db_chunk.id,
                text=chunk,
                embedding=embedding,
                metadata={
                    "document_id": document.id,
                    "chunk_index": index,
                    "title": document.title,
                },
            )

        return {
            "text": text,
            "chunks": len(chunks),
        }
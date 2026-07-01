import re


class ChunkService:
    """
    Handles splitting extracted document text into chunks.
    """

    @staticmethod
    def clean_text(text: str) -> str:
        # Remove extra whitespace
        text = re.sub(r"\s+", " ", text)
        return text.strip()

    @staticmethod
    def split_into_chunks(text: str, chunk_size: int = 500):
        text = ChunkService.clean_text(text)

        words = text.split()

        chunks = []
        current_chunk = []

        current_length = 0

        for word in words:
            current_chunk.append(word)
            current_length += len(word) + 1

            if current_length >= chunk_size:
                chunks.append(" ".join(current_chunk))
                current_chunk = []
                current_length = 0

        if current_chunk:
            chunks.append(" ".join(current_chunk))

        return chunks
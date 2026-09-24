"""
Extracts raw text from uploaded documents (PDF, DOCX, TXT) and returns
LangChain Document objects with metadata attached (filename, page number).
"""
import os
from langchain_community.document_loaders import PyPDFLoader
from langchain_core.documents import Document


def load_document_text(file_path: str, extension: str, original_filename: str) -> list[Document] :
    """
    Load and extract text from a file based on its extension.

    Args:
        file_path: full path to the saved file on disk
        extension: file extension, e.g. ".pdf", ".docx", ".txt"
        original_filename: the user's original filename, stored in metadata
                            so we always know which document a chunk came from

    Returns:
        A list of LangChain Document objects, each containing page_content
        and metadata (source filename, page number if applicable)

    Raises:
        ValueError: if the extension is unsupported
        Exception: if the file is corrupted or cannot be parsed
    """

          
    extension = extension.lower()
    
    if extension == '.pdf':
        return _load_pdf(file_path, original_filename)
    else:
        raise ValueError("Unsupported extension")

def _load_pdf(file_path: str, original_filename: str) -> list[Document]:
    try:
        
        loader = PyPDFLoader(file_path)
        pages = loader.load()
        for index, page in enumerate(pages):
            page.metadata['source_filename'] = original_filename
            page.metadata['page_number'] = index+1
    
    except Exception as e:
        raise Exception(f"Failed to parse : {e}")

    return pages

print(load_document_text('E:/github/LLM/llm_pdf_qa_chatbot/llm_pdf_qa_chatbot/backend/uploads/6ff5a_Enterprise_PDF_AI_Assistant_Roadmap.pdf', '.pdf', '6ff5a_Enterprise_PDF_AI_Assistant_Roadmap.pdf'))

    
    

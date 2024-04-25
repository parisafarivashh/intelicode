from langchain_community.document_transformers import DoctranTextTranslator
from langchain_core.documents import Document


def translator(body: str, translate_to) -> str:
    documents = [Document(page_content=body)]
    qa_translator = DoctranTextTranslator(language=translate_to)
    translated_document = qa_translator.transform_documents(documents)
    print(translated_document[0].page_content)
    return translated_document[0].page_content


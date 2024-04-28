from langchain.chains.conversation.base import ConversationChain
from langchain_community.document_transformers import DoctranTextTranslator
from langchain_core.documents import Document
from langchain.chains.conversation.memory import ConversationBufferMemory
from langchain.chains import LLMChain
from langchain_core.prompts import PromptTemplate
from langchain_community.llms import OpenAI


def translator(body: str, translate_to) -> str:
    documents = [Document(page_content=body)]
    qa_translator = DoctranTextTranslator(language=translate_to)
    translated_document = qa_translator.transform_documents(documents)
    return translated_document[0].page_content


def conversation(question: str) -> str:
    memory = ConversationBufferMemory()
    conversation = ConversationChain(
        llm=OpenAI(),
        memory=memory,
        verbose=True,
    )

    result = conversation.predict(input=question)
    memory.save_context({"input": question}, {"output": result})
    return result


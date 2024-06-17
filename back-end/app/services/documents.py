import os
from fastapi import File
from llama_index.embeddings.openai import OpenAIEmbedding
from llama_index.core import (
    SimpleDirectoryReader, 
    StorageContext, 
    VectorStoreIndex, 
    load_index_from_storage,
)
from index import PROJECT_ROOT_PATH
from llama_index.llms.openai import OpenAI
from llama_index.core import Settings
from app.models.document import Document
from app.models.metadata import Metadata

TEMP_UPLOAD_DIR = "/tmp/uploaded_docs"
LOCAL_DOCUMENTS_STORAGE_DIR = PROJECT_ROOT_PATH + "/llama-index/storage/documents"
LOCAL_DOCUMENT_STORAGE_PATH = PROJECT_ROOT_PATH + "/storage"

open_ai_key = os.environ['OPEN_AI_KEY']

llm = OpenAI(temperature=0, model="gpt-3.5-turbo", api_key=open_ai_key)
Settings.llm = llm
Settings.chunk_size = 512


async def create_document_from_file(file: File):
    try:
        os.makedirs(TEMP_UPLOAD_DIR, exist_ok=True) #exist_ok throws an error if the directory already exists

        # Create a temporary file location from filename
        temp_file_location = os.path.join(TEMP_UPLOAD_DIR, file.filename)

        with open(temp_file_location, "wb") as f:
            f.write(await file.read())

        # Create the reader from the entire directory
        reader = SimpleDirectoryReader(input_dir=TEMP_UPLOAD_DIR)
        documents = reader.load_data() # create the documents by loading in the data

        # Clean up the temporary file
        os.remove(temp_file_location)

        return documents[0]
    except Exception as err:
        # Clean up the temporary file
        os.remove(temp_file_location)
        raise

def get_index_storage_path():
    return LOCAL_DOCUMENTS_STORAGE_DIR


def create_empty_vector_store_index():
    embed_model = OpenAIEmbedding(api_key=open_ai_key)
    vector_index = VectorStoreIndex.from_documents([], embed_model=embed_model)
    return vector_index

def get_or_create_documents_storage_context():
    path = get_index_storage_path()
    storage_context = None

    # create an initial index
    vector_index = create_empty_vector_store_index()

    try:
        # attempt to get existing storage context
        storage_context = StorageContext.from_defaults(persist_dir = path)
    except Exception as err:
        # create new context if one does not exist
        storage_context = StorageContext.from_defaults(vector_store=vector_index.vector_store)
        storage_context.persist(persist_dir=path)
    
    return storage_context

def get_or_create_documents_store_index():
    storage_context = get_or_create_documents_storage_context()
    index = load_index_from_storage(storage_context=storage_context)
    return storage_context.index_store


def create_vector_index_from_directory():
    try:
        # Create the reader from the entire directory
        reader = SimpleDirectoryReader(input_dir=LOCAL_DOCUMENT_STORAGE_PATH)
        documents = reader.load_data() # create the documents by loading in the data
    except Exception as e:
        # handle empty directory by initializing empty docs
        documents = []

    # Create the vector store index
    embed_model = OpenAIEmbedding(api_key=open_ai_key)
    vector_index = VectorStoreIndex.from_documents(documents, embed_model=embed_model)
    return vector_index

async def save_file_to_local_storage(file):
    # Ensure the directory exists
    if not os.path.exists(LOCAL_DOCUMENT_STORAGE_PATH):
        os.makedirs(LOCAL_DOCUMENT_STORAGE_PATH)

    # Create the full path to save the file
    file_path = os.path.join(LOCAL_DOCUMENT_STORAGE_PATH, file.filename)

    # Write the file to local storage
    with open(file_path, 'wb') as f:
        f.write(await file.read())

    print(f"File saved to {file_path}")

def get_combined_document_metadata():
    documents = Document.get_all()
    document_items = documents.items

    metadata = Metadata.get_all()
    metadata_items = metadata.items

    documents_dict = {doc.id: doc for doc in document_items}

    # Join metadata with corresponding documents
    joined_data = []
    for item in metadata_items:
        document_id = item.document_id
        document = documents_dict.get(document_id)
        if document:
            joined_data.append({
                "metadata": item,
                "document": document
            })

    return joined_data
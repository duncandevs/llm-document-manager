import os
from fastapi import FastAPI, File, UploadFile, HTTPException, Request
from fastapi.middleware.cors import CORSMiddleware
from llama_index.core import SimpleDirectoryReader

from app.models.api import ACCEPTED_MIME_TYPES
from app.models.document import Document
from app.models.metadata import Metadata
from app.queries.metadata_query import MetadataQuery
from app.clients.pocketbase import pb
from app.queries.document_retrieval_query import DocumentRetrievalQuery
from app.services.documents import (
    create_document_from_file, 
    get_or_create_documents_store_index,
    create_vector_index_from_directory,
    save_file_to_local_storage,
    get_combined_document_metadata
)
from app.queries.base import (
    llm_get_query_response,
    llm_get_document_id,
)

app = FastAPI()

# Configuring CORS, Add Client URLS Below
origins = [
    "http://localhost:3001", 
    "http://localhost:3000", 
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/api/v1/documents/metadata")
async def create_document_metadata(file: UploadFile = File(...)):
    if file.content_type not in ACCEPTED_MIME_TYPES:
        raise HTTPException(status_code=400, detail="Invalid file type. Only PDF files are allowed.")

    document = await create_document_from_file(file)

    # Generate the llm query prompt and call it to get the document metadata
    query = MetadataQuery(text=document.text, filename=file.filename)
    query_results = query.call_llm()

    # Create the Document DB record
    document = Document(
        text=document.text,
        file_name= file.filename
    ).save_record()


    file_extension = Metadata.get_file_extension(
        filename=file.filename
    )

    # Create the Metadata DB record
    metadata = Metadata(
        document_id=document.id,
        actors=query_results.actors,
        summary=query_results.summary,
        label=query_results.label,
        tags=query_results.tags,
        source=query_results.source,
        is_company_wide_doc=query_results.is_company_wide_doc,
        file_extension=file_extension
    ).save_record()

    # Return Json of the metadata
    return { "metadata": metadata }


@app.post('/api/v1/documents')
async def upload_document(file: UploadFile = File(...)):
    if file.content_type not in ACCEPTED_MIME_TYPES:
        raise HTTPException(status_code=400, detail="Invalid file type. Only PDF files are allowed.")
    try:
        saved_file = await save_file_to_local_storage(file)
    except Exception as e:
        raise HTTPException(status_code=500, detail="Failed to save file, please check server for more details.")
    
    return 'OK'

@app.post('/api/v1/documents/query')
async def query_documents(req: Request):
    # get query from request body
    body = await req.json()
    query = body['query']

    # create vector index from document storage
    index = create_vector_index_from_directory()
    query_engine = index.as_query_engine()

    # create query and return response
    response = query_engine.query(query)
    return response

@app.get('/api/v1/documents')
async def get_documents():
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

    return {'items': joined_data}


@app.get('/api/v1/user/query')
async def user_query(req: Request):
    # body = await req.json()
    # query = body['query']
    query = "Show me some talking points which I can bring up for Alex's next performance review?"
    combined_document_data = get_combined_document_metadata()
    
    prompt = f"given the following user query: {query} pick out the document id of the most relevant document given the following sets of documents: {combined_document_data}"
    response_one = llm_get_document_id(prompt)
    document_id = response_one.document_id

    document = Document.get_by_id(document_id)

    final_prompt = f"given the following user question: {query} and the following document: {document} answer the user prompt, provide details from the document"
    response_two = llm_get_query_response(prompt)

    return {'result': response_two}

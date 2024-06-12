import os
from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from llama_index.core import SimpleDirectoryReader

from app.models.api import ACCEPTED_MIME_TYPES
from app.models.document import Document
from app.models.metadata import Metadata
from app.queries.metadata_query import MetadataQuery
from app.clients.pocketbase import pb


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
async def upload_document(file: UploadFile = File(...)):
    if file.content_type not in ACCEPTED_MIME_TYPES:
        raise HTTPException(status_code=400, detail="Invalid file type. Only PDF files are allowed.")

    # Create a temporary directory
    temp_dir = f"/tmp/uploaded_docs"
    os.makedirs(temp_dir, exist_ok=True)
    
    # Save the uploaded doc to a temporary location
    temp_file_location = os.path.join(temp_dir, file.filename)

    with open(temp_file_location, "wb") as f:
        f.write(await file.read())
    
    # Creates documents from the temp dir -> can parse more than one doc at a time if needed
    reader = SimpleDirectoryReader(input_dir=temp_dir)
    documents = reader.load_data()

    document = documents[0]

    # Clean up the temporary file
    os.remove(temp_file_location)

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
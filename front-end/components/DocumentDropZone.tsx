"use client";
import React, { useState } from 'react';
import {useDropzone} from 'react-dropzone';
import { Button } from "@/components/ui/button";
import { AlertError } from "@/components/AlertError";
import { uploadDocumentByFile } from "@/domains/documents/services";
import {
  Accordion,
  AccordionContent,
  AccordionItem,
  AccordionTrigger,
} from "@/components/ui/accordion";

const ACCEPTED_FILE_TYPES = {
  'application/pdf': ['.pdf'],
  'application/msword': ['.doc', '.docx'],
  'application/vnd.ms-excel': ['.xls', '.xlsx'],
  'text/plain': ['.txt'],
  'text/csv': ['.csv']
};

export const DocumentDropZone = () => {
    const [metadata, setMetadata] = useState(null);
    const [uploadError, setUploadError ] = useState("");
    const [isLoading, setIsLoading ] = useState(false);
    const {acceptedFiles, getRootProps, getInputProps, fileRejections} = useDropzone({
        accept: ACCEPTED_FILE_TYPES
    });  

    const files = acceptedFiles.map(file => (
      <li key={file.path}>
        <p className='text-sm text-gray-500'>{file.path} - {file.size} bytes</p>
      </li>
    ));

    const handleSubmit = async () => {
        setUploadError("");
        setIsLoading(true);

        try {
          const result = await uploadDocumentByFile(acceptedFiles[0]);
          setMetadata(result);
        } catch (error) {
          setUploadError('Failed to upload document by file')
        };

        setIsLoading(false);
    };

    const clearDocument = () => {
      setMetadata(null)
      setIsLoading(false)
      setUploadError('')
    };

    if(metadata) {
      return <div className='flex flex-col items-center mb-10'>
          <p>Document Uploaded Successfully</p>
          <div className='min-w-[300px] mt-10 mb-10'>
            <Accordion type="single" collapsible className="w-full">
              <AccordionItem value="item-1">
                <AccordionTrigger>View Metadata</AccordionTrigger>
                <AccordionContent>
                  <pre className="mt-2 w-[800px] rounded-md bg-slate-950 p-4 overflow-auto">
                    <code className="text-white">{JSON.stringify(metadata, null, 2)}</code>
                  </pre>  
                </AccordionContent>
              </AccordionItem>
            </Accordion>
          </div>
          <Button className='mx-auto' onClick={clearDocument} disabled={files.length === 0}>Try Another Doc</Button>
      </div>
    }

    return (
      <section className="container">
        <div className='flex flex-col m-auto justify-center items-center mt-[10%] space-y-6'>
            <div {...getRootProps({className: 'dropzone'})}>
                <div className='flex h-[200px] w-[500px] items-center justify-center rounded-md border border-dashed text-sm hover:border-blue-400'>
                    <input {...getInputProps()}/>
                    <p className='text-muted-foreground text-md'>Drag & drop some files here, or click to select files</p>
                </div>
            </div>
            <div>
                <h4 className='text-center'>File</h4>
                <ul>{files}</ul>
            </div>
            {!isLoading && <Button onClick={handleSubmit} disabled={files.length === 0}>Upload</Button>}
            {isLoading && <p>Uploading...</p>}
            {fileRejections && <p className='text-xs text-red-400'>{fileRejections[0]?.errors[0].message}</p>}
            <AlertError isShown={!!uploadError} description={uploadError} className='mt-6 w-[500px] m-auto'/>
        </div>
      </section>
    );
};
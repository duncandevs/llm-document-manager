import axios from 'axios';
import mime from  'mime-types';

// Fetch document results
const BASE_URL = 'http://localhost:8000';

export interface UploadDocumentQueryProps {
    formData: FormData;
};

export const uploadDocumentQuery = async ({ formData }: UploadDocumentQueryProps) => {
    const url = BASE_URL + '/api/v1/documents/metadata';
    const file = formData.get('file') as File;

    if (!file) throw new Error('No file provided in formData');

    // Get the MIME type of the file
    const mimeType = mime.lookup(file.name) || 'application/octet-stream';
    const headers = {
        'Content-Type': mimeType
    };

    const request = {
        method: 'POST',
        url,
        headers,
        data: formData
    };
    return axios(request);
};


export const getDocuments = async () => {
    const url = BASE_URL + '/api/v1/documents';
    return axios.get(url)
};
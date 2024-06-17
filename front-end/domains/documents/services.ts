import { uploadDocumentQuery, getDocuments } from './api';

export const uploadDocumentByFile = async (file: File) => {
    try {
        const formData = new FormData();
        formData.append('file', file);

        const results = await uploadDocumentQuery({ formData });
        if(!results.data) throw Error();

        return results.data
    } catch (error) {
        throw Error('Failed to upload document by file')
    }
};

export const getMergedDocuments = async () => {
    try {
        const results = await getDocuments();
        if(!results) throw Error('Failed to fetch document data')
        return results?.data?.items || []
    } catch (error) {
        throw(error)
    };
};
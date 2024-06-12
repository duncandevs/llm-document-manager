import { DocumentDropZone } from "@/components/DocumentDropZone"
import { UploadIcon} from 'lucide-react'

export default function Page () {
    return <div>
        <head className="flex flex-row items-center p-4 space-x-4">
            <UploadIcon/>
            <p>Document Upload</p>
        </head>
        <DocumentDropZone />
    </div>
}
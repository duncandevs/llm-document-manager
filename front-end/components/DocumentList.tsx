"use client"
import { getMergedDocuments } from "@/domains/documents/services"
import { useEffect, useState } from "react";

export const DocumentList = () => {
    const [label, setLabel] = useState("");
    const [documents, setDocuments] = useState([]);
    const [filteredDocs, setFilteredDocs] = useState([])

    useEffect(()=>{
        getMergedDocuments().then((res)=>{
            setDocuments(res)
            setFilteredDocs(res)
        })
    }, [])

    const handleLabelChange = (e) => {
        const val = e.target.value;
        setLabel(val);
    };

    const handleLabelFilter = () => {
        const newDocs = documents?.filter((doc)=>{
            if(!label) return !!doc
            return doc.metadata.label === label
        });
        setFilteredDocs(newDocs)
    }

    return (
        <div>
            <h2>Documents</h2>
            <input value={label} onChange={handleLabelChange} className="border border-gray-400"/>
            <button onClick={handleLabelFilter}>Filter</button>
            <p>{label}</p>
            {filteredDocs?.map((item)=><ul className="space-y-4 text-left">
                <li>
                    <p className="text-xl">{item?.document?.file_name}</p>
                    <p className="text-sm">{item?.metadata?.label}</p>
                </li>
            </ul>)}
        </div>
    )
}
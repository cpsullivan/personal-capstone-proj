import { useState } from 'react'
import { useNavigate } from "react-router-dom"
import './CreateARs.css'


function CreateActionRequest() {

    const navigate = useNavigate()

    const [actionRequestTitle, setActionRequestTitle] = useState()
    const [createdOn, setCreatedOn] = useState()
    const [action, setAction] = useState()
    const [dueDate, setDueDate] = useState()
    const [comments, setComments] = useState()
    const [documents, setDocuments] = useState()
    const [errors, setErrors] = useState()

    const handleActionRequestTitleChange = (e) => setActionRequestTitle(e.target.value)
    const handleCreatedOn = (e) => setCreatedOn(e.target.value)
    const handleActionChange = (e) => setAction(e.target.value)
    const handleDueDateChange = (e) => setDueDate(e.target.value)
    const handleCommentsChange = (e) => setComments(e.target.value)
    const handleDocumentsChange = (e) => setDocuments(e.target.files[0])

    const handleSubmit = (e) => {
        e.preventDefault()
        const actionRequestObject = {
            action_request_title: actionRequestTitle,
            created_on: createdOn,
            action: action,
            due_date: dueDate,
            comments: comments,
            documents: documents
        }
        addActionRequest(actionRequestObject)
    }

    const addActionRequest = async (actionRequestObject) => {
        const base_url = import.meta.env.VITE_BASE_URL
        const url = `http://${base_url}/api/`
        let formData = new FormData()
        formData.append('action_request_title', actionRequestObject.actionRequestTitle)
        formData.append('created_on', actionRequestObject.createdOn)
        formData.append('action', actionRequestObject.action)
        formData.append('due_date', actionRequestObject.dueDate)
        formData.append('comments', actionRequestObject.comments)
        formData.append('documents', actionRequestObject.documents, actionRequestObject.documents.name)
        const context = {
            method: 'POST',
            body: formData
        }
        const resp = await fetch(url, context)
        const body = await resp.json()
        if (resp.status === 400) {
            setErrors(body)
        } else {
            navigate('/')
        }
    }

    return(
        <>
            <h2>Create Action Request</h2>
            {errors && <h4>{JSON.stringify(errors)}</h4>}
            <div>
                <label htmlFor='actionRequestTitle'>Action Request Title:</label>
                <input value={actionRequestTitle} name='actionRequestTitle' onChange={handleActionRequestTitleChange}></input>
            </div>
            <div>
                <label htmlFor='createdOn'>Created On:</label>
                <input value={createdOn} name='createdOn' onChange={handleCreatedOn}></input>
            </div>
            <div>
                <label htmlFor='action'>Action:</label>
                <input value={action} name='action' onChange={handleActionChange}></input>
            </div>
            <div>
                <label htmlFor='due_date'>Due Date:</label>
                <input value={dueDate} name='due_date' onChange={handleDueDateChange}></input>
            </div>
            <div>
                <label htmlFor='comments'>Comments:</label>
                <input value={comments} name='comments' onChange={handleCommentsChange}></input>
            </div>
            <div>
                <label htmlFor='documents'>Documents:</label>
                <input value={documents} name='documents' onChange={handleDocumentsChange}></input>
            </div>
            <div>
                <button onClick={handleSubmit}>Submit</button>
            </div>
        </>
    )
}
export default CreateActionRequest
import { useEffect, useState } from 'react'

function ListActionRequests() {

  const [action_requests, setARs] = useState([])

  useEffect( () => {
    async function getARs() {
      const base_url = import.meta.env.VITE_BASE_URL
      const res = await fetch(`http://${base_url}/api/`)
      const body = await res.json()
      setARs(body.result)
    }
    getARs()
  }, [])

  const createActionRequestList = () => {
    return action_requests.map( w => {
      return (
        <>
        <h2 key={w.action_request_title}>{w.action_request_title}</h2>
        </>
      )
  })
  }


  return(
    <>
      <h2>List Action Requests</h2>
      {action_requests && createActionRequestList()}
    </>
  )
}

export default ListActionRequests
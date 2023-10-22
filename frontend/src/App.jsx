import './App.css';
import { HashRouter, Routes, Route, Link } from 'react-router-dom'
import ListARs from './components/ListActionRequests'
import CreateAR from './components/CreateActionRequest'
import './App.css'

function App() {

  return (
    <div className="App">
      <HashRouter>
        <h1>Action Requests</h1>
        <Link to='/all-action-requests'>List Action Requests</Link>
        <br></br>
        <Link to='/create'>Create Action Request</Link>
        <Routes>
          <Route path='/all-action-requests' element={ <ListActionRequests />} />
          <Route path='/create' element={ <CreateActionRequest />} />
        </Routes>
      </HashRouter>
    </div>

  )
}

export default App

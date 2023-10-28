import './App.css';
import { HashRouter, Routes, Route, Link } from 'react-router-dom';
import ListActionRequests from './components/ListARs';
import CreateActionRequest from './components/CreateARs';


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

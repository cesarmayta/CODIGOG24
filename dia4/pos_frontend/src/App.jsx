import {
  BrowserRouter,Routes,Route
} from 'react-router-dom'
import PosPos from './modulos/pos/pages/PosPos';
import Auth from './modulos/auth/pages/Auth';
import Admin from './modulos/admin/pages/Admin';

const App = () => {
  return (
    <BrowserRouter>
      <Routes>
        <Route path='/' element={<PosPos/>}/>
        <Route path='/auth' element={<Auth/>}/>
        <Route path='/admin' element={<Admin/>}/>
      </Routes>
    </BrowserRouter>
  )
}

export default App;

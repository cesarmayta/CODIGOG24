import {
  BrowserRouter,Routes,Route
} from 'react-router-dom'
import Pos from './modulos/pos/pages/Pos';
import Auth from './modulos/auth/pages/Auth';
import Admin from './modulos/admin/pages/Admin';

const App = () => {
  return (
    <BrowserRouter>
      <Routes>
        <Route path='/' element={<Pos/>}/>
        <Route path='/auth' element={<Auth/>}/>
        <Route path='/admin' element={<Admin/>}/>
      </Routes>
    </BrowserRouter>
  )
}

export default App;

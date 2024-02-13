import { createBrowserRouter } from "react-router-dom";
import Home from '../pages/Home';
import Marca from '../pages/Marca';

const router = createBrowserRouter([
    {
        path:"/",
        element:<Home/>
    },
    {
        path:"/marca",
        element:<Marca/>
    }
])

export default router;
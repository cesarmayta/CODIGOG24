import { createBrowserRouter } from "react-router-dom";
import Home from "../pages/home";
import Cart from "../pages/cart";
import App from "../App";

const router = createBrowserRouter([
    {
        path:'/',
        element:<App/>,
        children: [
            {
                index: true,
                element:<Home/>
            },
            {
                path:'/cart',
                element:<Cart/>
            }
        ]
    },
    
])

export default router
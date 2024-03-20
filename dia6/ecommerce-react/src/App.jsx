import MainFooter from "./components/MainFooter"
import MainHeader from "./components/MainHeader"
import { Outlet } from "react-router-dom"

const App = () => {
    return(
        <>
        <div className="site">
            <MainHeader/>
            <Outlet/>
            <MainFooter/>
        </div>
        </>
    )
}

export default App
import MainFooter from "../components/MainFooter"
import MainHeader from "../components/MainHeader"
import SiteContent from "../components/SiteContent"

const Home = () => {
    return(
        <>
        <div className="site">
            <MainHeader/>
            <SiteContent/>
            <MainFooter/>
        </div>
        </>
    )
}

export default Home
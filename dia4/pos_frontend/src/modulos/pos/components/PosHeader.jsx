import logo from '../../../assets/logo.svg';
import search from '../../../assets/search.svg';

const PosHeader = () =>{
    return(
        <header className="header">
            <div className="header__logo">
            <img src={logo} alt="" />
            </div>
            <div className="header__buscador">
            <img src={search} alt="" />
            <input type="text" className="header__input" placeholder="Busca un término" />
            </div>
            <div className="header__usuario">
            <img src="https://randomuser.me/api/portraits/men/90.jpg" alt="" />
            <span>Usuario</span>
            </div>
        </header>
    )
}

export default PosHeader;
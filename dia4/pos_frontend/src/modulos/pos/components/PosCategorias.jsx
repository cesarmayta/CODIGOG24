import plato_blanco from '../../../assets/plato_blanco.svg';
const PosCategorias = () =>{
    return (
        <nav className="menu">
            <ul className="menu__lista">
                <li className="active">
                    <img src={plato_blanco} alt="" />
                    <span>Entradas</span>
                </li>
            </ul>
        </nav>
    )
}

export default PosCategorias;
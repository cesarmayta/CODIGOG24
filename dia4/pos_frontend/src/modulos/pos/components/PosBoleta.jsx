const PosBoleta = () =>{
    return (
        <div className="boleta">
          <h3>Pedido Mesa: &nbsp;<span className="color-secundario">01</span></h3>
          <hr/>
          <div className="comanda">
            <h4 className="comanda__mesa">Mesa 01</h4>
            <hr />

            <ul className="comanda__lista">
              <li className="comanda__item">
                <p className="comanda__nombre">
                  <span><strong>Arroz Chaufa de Pollo</strong></span>
                  <span>Precio: S/ 35.00</span>
                </p>
                <p className="comanda__cantidad">01</p>
                <p className="comanda__precio">
                  <strong>S/ 35.00</strong>
                </p>
              </li>
            </ul>
            <button className="boton boton-success boton-block">PAGAR</button>
          </div>
        </div>
    )
}

export default PosBoleta;
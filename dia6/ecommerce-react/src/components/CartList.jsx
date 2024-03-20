import { CartContext } from '../context/CartContext'
import { useContext } from "react"
import CartItem from './CartItem'

const CartList = () =>{
    const {state} = useContext(CartContext)
    return(
        <div id="content" className="site-content">
            <div id="primary" className="content-area width-normal">
                <main id="main" className="site-main">
                    <div className="cont maincont">
                        <h1 className="maincont-ttl">Cart</h1>
                        <ul className="b-crumbs">
                            <li><a href="index.html">Home</a></li>
                            <li>Cart</li>
                        </ul>
                        <div className="page-styling">
                            <div className="woocommerce prod-litems section-list">
                                {state.cart.map((prod)=>(
                                    <CartItem key={prod.id} product={prod}/>
                                ))}
                            </div>
                            <div className="cart-actions">
                                <div className="coupon">
                                    <input type="text" placeholder="Coupon code"/>
                                        <input type="submit" className="button" value="Apply"/>
                                        </div>
                                        <div className="cart-collaterals">
                                            <a href="#" className="checkout-button button">Proceed to checkout</a>
                                            <div className="order-total">
                                                <p className="cart-totals-ttl">Total</p>
                                                <p className="cart-totals-val">$510.00</p>
                                            </div>
                                        </div>
                                </div>
                        </div>
                    </div>
                </main>
            </div>
        </div>
    )
}

export default CartList
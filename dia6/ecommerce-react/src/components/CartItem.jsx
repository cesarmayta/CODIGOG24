const CartItem = ({product}) =>{
    return(
        <article className="prod-li sectls">
                                    <div className="prod-li-inner">
                                        <a href="product.html" className="prod-li-img">
                                            <img src={product.image} alt=""/>
                                        </a>
                                        <div className="prod-li-cont">
                                            <div className="prod-li-ttl-wrap">
                                                <p>
                                                    <a href="#">Lighting</a>
                                                </p>
                                                <h3><a href="product.html">{product.name}</a></h3>
                                            </div>
                                            <div className="prod-li-prices">
                                                <div className="prod-li-price-wrap">
                                                    <p>Price</p>
                                                    <p className="prod-li-price">$ {product.price}</p>
                                                </div>
                                                <div className="prod-li-qnt-wrap">
                                                    <p className="qnt-wrap prod-li-qnt">
                                                        <a href="#" className="qnt-plus prod-li-plus"><i className="icon ion-arrow-up-b"></i></a>
                                                        <input type="text" value="1"/>
                                                            <a href="#" className="qnt-minus prod-li-minus"><i className="icon ion-arrow-down-b"></i></a>
                                                    </p>
                                                </div>
                                                <div className="prod-li-total-wrap">
                                                    <p>Total</p>
                                                    <p className="prod-li-total">$ {product.price}</p>
                                                </div>
                                            </div>
                                        </div>
                                        <div className="prod-li-info">
                                            <div className="prod-li-rating-wrap">
                                                <p data-rating="5" className="prod-li-rating">
                                                    <i className="rating-ico" title="1"></i><i className="rating-ico" title="2"></i><i className="rating-ico" title="3"></i><i className="rating-ico" title="4"></i><i className="rating-ico" title="5"></i>
                                                </p>
                                                <p className="prod-li-rating-count">12</p>
                                            </div>
                                            <p className="prod-li-add">
                                                <a href="#" className="button hover-label prod-addbtn"><i className="icon ion-close-round"></i><span>Remove</span></a>
                                            </p>
                                            <p className="prod-li-compare">
                                                <a href="compare.html" className="hover-label prod-li-compare-btn"><span>Compare</span><i className="icon ion-arrow-swap"></i></a>
                                            </p>
                                            <p className="prod-quickview">
                                                <a href="#" className="hover-label quick-view"><i className="icon ion-plus"></i><span>Quick View</span></a>
                                            </p>
                                            <div className="prod-li-favorites">
                                                <a href="wishlist.html" className="hover-label add_to_wishlist"><i className="icon ion-heart"></i><span>Add to Wishlist</span></a>
                                            </div>
                                            <p className="prod-li-information">
                                                <a href="#" className="hover-label"><i className="icon ion-more"></i><span>Show Information</span></a>
                                            </p>
                                        </div>
                                    </div>
                                    <div className="page-styling prod-li-informations">

                                        <dl className="prod-li-props">
                                            <dt>Brand:</dt>
                                            <dd><a href="#">AIR</a></dd>
                                            <dt>Weight:</dt>
                                            <dd>1 kg</dd>
                                            <dt>Dimensions:</dt>
                                            <dd>4 x 50 cm</dd>
                                            <dt>Сolor:</dt>
                                            <dd><a href="#" rel="tag">Black</a>, <a href="#" rel="tag">Green</a></dd>
                                            <dt>Manufacturer:</dt>
                                            <dd><a href="#">France</a></dd>
                                            <dt>Material:</dt>
                                            <dd><a href="#" rel="tag">Metall</a>, <a href="#" rel="tag">Plastic</a>, <a href="#" rel="tag">Rubber</a></dd>
                                        </dl>
                                    </div>
                                </article>
    )
}

export default CartItem
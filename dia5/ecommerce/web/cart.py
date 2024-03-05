class Cart:
    
    def __init__(self,request):
        self.request = request
        self.session = request.session
        cart = self.session.get('cart')
        total = self.session.get('cart_total')
        if not cart:
            cart = self.session['cart'] = {}
            total = self.session['cart_total'] = 0
            
        self.cart = cart
        self.total = float(total)
        
    def add(self,producto,cantidad,imagen_url):
        if (str(producto.id) not in self.cart.keys()):
            self.cart[producto.id] = {
                'producto_id':producto.id,
                'nombre':producto.nombre,
                'cantidad':cantidad,
                'precio':str(producto.precio),
                'imagen':imagen_url,
                'categoria':producto.categoria.nombre,
                'marca':producto.marca.nombre,
                'subtotal':str(cantidad * producto.precio)
            }
        else:
            for key,value in self.cart.items():
                if key == str(producto.id):
                    value['cantidad'] = value['cantidad']  + cantidad
                    value['subtotal'] = str(float(value['cantidad']) * float(value['precio']))
                    break           
            
        self.save()
        
    def delete(self,producto):
        if str(producto.id) in self.cart:
            del self.cart[str(producto.id)]
            self.save()  
            
    def clear(self):
        self.session['cart'] = {}
        self.session['cart_total'] = 0   
    
    def save(self):
        total = 0
        for key,value in self.cart.items():
            total += float(value['subtotal'])
            
        self.session['cart_total'] = total
        self.session['cart'] = self.cart
        self.session.modified = True
        
    
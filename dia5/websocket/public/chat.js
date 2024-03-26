const socket = io('http://localhost:5000')

let ouput = document.getElementById('output')
let mensaje = document.getElementById('mensaje')
let btn = document.getElementById('enviar')

btn.addEventListener('click',function(){
    socket.emit('mensajeCliente',{
        mensaje:mensaje.value
    })
})
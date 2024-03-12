function hola(nombre,primercallback){
    setTimeout(function(){
        console.log('Hola ' + nombre)
        primercallback(nombre)
    },1000)
}
let nombre = 'César';
hola(nombre,function(nombre){
    console.log('Adios ' + nombre);
});

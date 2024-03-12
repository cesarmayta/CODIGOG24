function hola(nombre,primercallback){
    setTimeout(function(){
        console.log('Hola ' + nombre)
        primercallback(nombre)
    },1000)
}

function hablar(nombre,segundocallback){
    setTimeout(function(){
        console.log("como estas " + nombre)
        segundocallback(nombre)
    },1000)
}

let nombre = 'César';
hola(nombre,function(nombre){
    hablar(nombre,function(nombre){
        setTimeout(function(){
            console.log("Adios " + nombre)
        },1000)
    })
});

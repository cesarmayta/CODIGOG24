const os = require('os');

const procesador = os.arch();
console.log('tipo procesador : ' + procesador);

const sistema = os.platform();
console.log('sistema operativo : ' + sistema);

const cpu = os.cpus();
console.log('modelo procesador : ' + cpu[0].model);

const memoria = os.totalmem();
console.log('memoria ram : '+ memoria);

/* implementar con promesas un función que retorne la memoria
en kb,mb y gb
1024 bytes = 1kb
1024 kb = 1mb
1024 mb = 1gb
*/
function calcularMemoria(capacidad,tipo){
    return new Promise((res,rej)=>{
        let memoriaConvertida = capacidad / 1024
        console.log(`MEMORIA EN ${tipo} : ${memoriaConvertida.toFixed(2)}`);
        res(memoriaConvertida);
        rej('error...')
    })
}

calcularMemoria(memoria,'KB')
    .then((kb)=>calcularMemoria(kb,'MB'))
    .then((mb)=>calcularMemoria(mb,'GB'))

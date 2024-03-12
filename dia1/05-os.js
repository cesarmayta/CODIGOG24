const os = require('os');

const procesador = os.arch();
console.log('tipo procesador : ' + procesador);

const sistema = os.platform();
console.log('sistema operativo : ' + sistema);

const cpu = os.cpus();
console.log('modelo procesador : ' + cpu[0].model);

const memoria = os.totalmem();
console.log('memoria ram : '+ memoria);
const express = require('express');
const bp = require('body-parser')

const app = express()
app.use(bp.urlencoded({extended: true}))
app.use(express.static('public'))

app.get('/',(req,res)=>{
    res.send('<h1><center>Mi primer servidor con express.js y Nodejs</center></h1>')
})

app.get('/api',(req,res)=>{
    res.json({
        'status':true,
        'message':'api rest activo con express'
    })
})

app.get('/saludo',(req,res)=>{
    let nombre = req.query.nombre;
    res.send(`<h1><center><i>Hola ${nombre}</i></center></h1>`);
})

app.get('/suma/:n1/:n2',(req,res)=>{
    const {n1,n2} = req.params;
    let suma = parseInt(n1) + parseInt(n2)
    res.send(`la suma de ${n1} + ${n2} es ${suma}`);
})

app.post('/calculadora',(req,res)=>{
    n1 = req.body.n1;
    n2 = req.body.n2;
    ope = req.body.ope;
    switch(ope){
        case '+':
            resultado = parseInt(n1) + parseInt(n2);
            res.send(`La suma de ${n1} + ${n2} es ${resultado}`);
            break;
        case '-':
            resultado = parseInt(n1) - parseInt(n2);
            res.send(`La resta de ${n1} - ${n2} es ${resultado}`);
            break;
        case 'x':
            resultado = parseInt(n1) * parseInt(n2);
            res.send(`La multiplicación de ${n1} x ${n2} es ${resultado}`);
            break;
        case '/':
            resultado = parseInt(n1) / parseInt(n2);
            res.send(`La división de ${n1} / ${n2} es ${resultado}`);
            break;
        default:
            res.send('No se encontro operación');
    }
})

app.listen(5000,()=>console.log('servidor en http://127.0.0.1:5000'))
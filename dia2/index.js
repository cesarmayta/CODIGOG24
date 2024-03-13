const express = require('express');

const app = express()

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

app.listen(5000,()=>console.log('servidor en http://127.0.0.1:5000'))
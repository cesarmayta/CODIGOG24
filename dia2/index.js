const express = require('express');

const app = express()

app.get('/',(req,res)=>{
    res.send('<h1><center>Mi primer servidor con express.js y Nodejs</center></h1>')
})

app.listen(5000,()=>console.log('servidor en http://127.0.0.1:5000'))
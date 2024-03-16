const express = require('express')
const {sequelize,Tarea} = require('./database')
const cors = require('cors')

const app = express()
app.use(cors())
app.use(express.json())

app.get('/tarea',(req,res)=>{
    Tarea.findAll()
    .then(function(result){
        res.json({
            status:true,
            content:result
        })
    })
})

app.listen(5000,()=>console.log('http://localhost:5000'))
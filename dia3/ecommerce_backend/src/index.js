const express = require('express')
const {config} = require('./config')

const app = express()
app.use(express.json())

app.get('/',(req,res)=>{
    res.json({
        'status':true,
        'message':'api rest ecommerce version 1.0'
    })
})

app.listen(config.port,
    ()=>console.log(`http://127.0.0.1:${config.port}`))
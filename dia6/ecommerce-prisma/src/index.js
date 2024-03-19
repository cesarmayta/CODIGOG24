const express = require('express')
const {config} = require('./config')

const app = express()
app.use(express.json())

app.get('/',(req,res)=>{
    res.json({
        'status':true,
        'message':'api rest con prisma'
    })
})

app.listen(config.port,()=>console.log('http://127.0.0.1:'+config.port))
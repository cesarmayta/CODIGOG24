const express = require('express')
const {config} = require('./config')

const categoryApi = require('./routes/category.routes')
const productApi = require('./routes/product.routes')

const app = express()
app.use(express.json())

app.get('/',(req,res)=>{
    res.json({
        'status':true,
        'message':'api rest con prisma'
    })
})

categoryApi(app)
productApi(app)

app.listen(config.port,()=>console.log('http://127.0.0.1:'+config.port))
const express = require('express')
const {config} = require('./config')

const categoryApi = require('./routes/category.routes')

const app = express()
/******** MIDDLEWARES **********/
app.use(express.json())
app.use(function(req,res,next){
    const timeElapsed = Date.now()
    const today = new Date(timeElapsed)
    console.log('ejecutado a las ',today.toISOString())
    next()
})

app.use('/usuario',(req,res,next)=>{
    console.log('tipo de request',req.method)
    next()
})

app.get('/',(req,res)=>{
    res.json({
        'status':true,
        'message':'api rest ecommerce version 1.0'
    })
})

app.get('/usuario',(req,res)=>{
    console.log(a + 3)
    res.json({
        nombre:'cesar'
    })
})



categoryApi(app)


//MIDDLEWARES DE ERRORES
app.use(function(err,req,res,next){
    console.error(err.stack)
    res.status(500).json({
        'message':err.stack
    })
})

app.listen(config.port,
    ()=>console.log(`http://127.0.0.1:${config.port}`))
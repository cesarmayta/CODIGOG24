const express = require('express')
const {config} = require('./config')
const boom = require('@hapi/boom')


const categoryApi = require('./routes/category.routes')
const {errorHandler,boomErrorHandler} = require('./middlewares/error.handler')
const morgan = require('morgan')

const app = express()
/******** MIDDLEWARES **********/
app.use(express.json())
app.use(morgan('combined'))

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
    try{
        console.log(a + 3)
        res.json({
        nombre:'cesar'
    })
    }catch(err){
        res.status(500).json(boom.badData(`error : ${err.message}`))
    }
    
})



categoryApi(app)


//MIDDLEWARES DE ERRORES
app.use(errorHandler)
app.use(boomErrorHandler)

app.listen(config.port,
    ()=>console.log(`http://127.0.0.1:${config.port}`))
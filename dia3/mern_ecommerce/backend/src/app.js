const express = require('express')
const {config} = require('./config')
const cors = require('cors')

const fileUpload = require('express-fileupload')

const app = express()

app.use(cors())
app.use(fileUpload())
app.use(express.json())

app.set('port',config.port)

app.get('/',(req,res)=>{
    res.json({
        "status":true,
        "message":"api rest ecommerce con mongodb"
    })
})

app.use('/categories',require('./routes/category.route'))
app.use('/user',require('./routes/user.route'))
app.use('/products',require('./routes/product.route'))

module.exports = app
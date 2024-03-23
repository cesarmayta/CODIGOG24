const express = require('express')
const {config} = require('../../config')

const cors = require('cors')

require('../../libs/mongoose.lib')

const app = express()

app.use(cors())
app.use(express.json())

app.get('/',(req,res)=>{
    res.json({
        'message':'mscatalog active'
    })
})

app.use('/categories',require('../../routes/category.route'))

app.listen(config.mscatalog.port,function(){
    console.log(`ms catalog http://127.0.0.1:${config.mscatalog.port}`)
})
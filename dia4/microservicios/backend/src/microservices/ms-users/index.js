const express = require('express')
const {config} = require('../../config')
const cors = require('cors')

require('../../libs/mongoose.lib')

const app = express()
app.use(cors())
app.use(express.json())

app.get('/',(req,res)=>{
    res.json({
        message:'ms users active'
    })
})

app.use('/user',require('../../routes/user.route'))

app.listen(config.msusers.port,function(){
    console.log(`ms users : http:127.0.0.1:${config.msusers.port}`)
})
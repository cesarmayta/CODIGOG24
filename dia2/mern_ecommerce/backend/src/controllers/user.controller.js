const userController = {}
const bcrypt = require('bcryptjs')
const userModel = require('../models/user.model')

userController.create = async (req,res)=>{
    try{
        const hash = await bcrypt.hash(req.body.password,10)
        re.body.password = hash
        const newUser = new userModel(req.body)
        await newUser.save()
        res.status(201).json({
            'id':newUser._id,
            'email':newUser.email
        })

    }catch{
        res.status(500).json({
            message:'error : ' + err.message
        })
    }
}

module.exports = userController

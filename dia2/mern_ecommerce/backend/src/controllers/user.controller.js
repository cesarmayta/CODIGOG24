const userController = {}
const bcrypt = require('bcrypt')
const userModel = require('../models/user.model')

userController.create = async (req,res)=>{
    try{
        const hash = await bcrypt.hash(req.body.password,10)
        req.body.password = hash
        const newUser = new userModel(req.body)
        await newUser.save()
        res.status(201).json({
            'id':newUser._id,
            'email':newUser.email
        })

    }catch(err){
        res.status(500).json({
            message:'error '+err.message
        })
    }
}

userController.getAll = async (req,res)=>{
    try{
        const users = await userModel.find({},'email isAdmin')
        res.status(200).json(users)
    }catch(err){
        res.status(500).json({
            message:'error '+err.message
        })
    }
}

userController.getOne = async (req,res)=>{
    try{
        const user = await userModel.findById(req.params.id)
        res.json({
            id:user._id,
            email:user.email,
            isAdmin:user.isAdmin
        })
    }catch(err){
        res.status(500).json({
            message:'error '+err.message
        })
    }
}

module.exports = userController

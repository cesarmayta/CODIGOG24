const express = require('express')
const {PrismaClient} = require('@prisma/client')


function categoryApi(app){
    const router = express.Router()
    app.use('/categories',router)

    const prisma = new PrismaClient()

    router.get('/',async function(req,res){
        try{
            const data = await prisma.tbl_category.findMany()
            res.status(200).json(data)

        }catch(err){
            res.status(500).json({
                'error':err
            })
        }
    })

    router.post('/',async function(req,res){
        try{
            const newData = await prisma.tbl_category.create({
                data:req.body
            })
            res.status(201).json(newData)
        }catch(err){
            res.status(500).json({
                'error':err
            })
        }
    })

    router.get('/:id',async (req,res)=>{
        try{
            const data = await prisma.tbl_category.findUnique({
                where:{
                    id:parseInt(req.params.id)
                }
            })
            res.status(200).json(data)
        }catch(err){
            res.status(500).json({
                'error':err
            })
        }
    })
}

module.exports = categoryApi
const express = require('express')
const {PrismaClient} = require('@prisma/client')


function productApi(app){
    const router = express.Router()
    app.use('/products',router)

    const prisma = new PrismaClient()

    router.get('/',async function(req,res){
        try{
            const data = await prisma.tbl_product.findMany()
            res.status(200).json(data)

        }catch(err){
            res.status(500).json({
                'error':err
            })
        }
    })

    router.post('/',async function(req,res){
        try{
            const newData = await prisma.tbl_product.create({
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
            const data = await prisma.tbl_product.findUnique({
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

    router.put('/:id',async (req,res)=>{
        try{
            const data = await prisma.tbl_product.update({
                where:{
                    id:parseInt(req.params.id)
                },
                data:req.body
            })
            res.status(200).json(data)
        }catch(err){
            res.status(500).json({
                'error':err
            })
        }
    })

    router.delete('/:id',async (req,res)=>{
        try{
            const data = await prisma.tbl_product.delete({
                where:{
                    id:parseInt(req.params.id)
                }
            })
            res.sendStatus(201)
        }catch(err){
            res.status(500).json({
                'error':err
            })
        }
    })
}

module.exports = productApi
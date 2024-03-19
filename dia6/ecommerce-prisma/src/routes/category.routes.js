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

    // router.get('/',async function(req,res){
    //     try{

    //     }catch(err){
    //         res.status(500).json({
    //             'error':err
    //         })
    //     }
    // })
}

module.exports = categoryApi
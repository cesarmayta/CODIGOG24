const express = require('express');

const mysqlConnection = require('./database');

const app = express();

app.get('/',(req,res)=>{
    res.json({
        'status':true,
        'content':'api rest activo con mysql'
    })
})

app.get('/tarea',(req,res)=>{
    mysqlConnection.query('select * from tarea',(err,rows,fields)=>{
        if(!err){
            context = {
                'status':true,
                'content':rows
            }
            res.json(context);
        }
        else{
            console.log(err);
        }
    })
    
})

app.get('/tarea/:id',(req,res)=>{
    const {id} = req.params;

    const query = 'select * from tarea where id=?'

    mysqlConnection.query(query,[id],(err,rows,fields)=>{
        if(!err){
            context = {
                'status':true,
                'content':rows
            }
            res.json(context);
        }
        else{
            console.log(err)
        }
    })
})

app.listen(5000,()=>console.log('http://127.0.0.1:5000'))
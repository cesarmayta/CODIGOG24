const mysql = require('mysql2');

const mysqlConnection = mysql.createConnection({
    host:'localhost',
    user:'root',
    password:'root',
    database:'db_tareas'
});

mysqlConnection.connect(function(err){
    if(err){
        console.error(err);
        return;
    }else{
        console.log('conectado a la bd');
    }
})

module.exports = mysqlConnection

/*
mysqlConnection.query('select * from tarea',(err,rows,fields)=>{
    console.log(rows);
})*/

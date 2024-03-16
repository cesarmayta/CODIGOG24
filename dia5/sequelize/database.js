const Sequelize = require('sequelize')

const sequelize = new Sequelize({
    dialect : 'sqlite',
    storage : './.db.sqlite'
})

sequelize.authenticate()
.then(()=>console.log('conectado a base de datos'))
.catch(err=>console.log('error : ',err))


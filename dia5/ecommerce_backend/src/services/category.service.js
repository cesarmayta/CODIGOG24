const MysqlLib = require('../lib/mysql')
const {models} = require('../lib/sequelize')

class CategoryService{

    constructor(){
        this.db = new MysqlLib()
    }

    async getAll(){
        //const query = 'select id,name from tbl_category'
        //const result = await this.db.querySql(query)
        const result = await models.Category.findAll()
        return result
    }

    async create({data}){
        const query = `insert into tbl_category(name)
                       values ('${data.name}')`
        await this.db.querySql(query)
        const queryLast = 'select id,name from tbl_category order by id desc limit 1'
        const result = await this.db.querySql(queryLast)
        return result
    }

    async getById(id){
        const query = `select id,name from tbl_category where id= '${id}'`
        const result = await this.db.querySql(query)
        return result
    }

    async update({data,id}){
        const query = `update tbl_category set
                       name = '${data.name}'
                       where id= ${id}`
        await this.db.querySql(query)
        const queryUpdated = `select id,name from tbl_category where id = ${id}`
        const result = await this.db.querySql(queryUpdated)
        return result
    }

    async delete(id){
        const query = `delete from tbl_category 
                       where id=${id}`
        await this.db.querySql(query)
        return true
    }
}

module.exports = CategoryService
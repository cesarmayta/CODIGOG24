const {Model,DataTypes,Sequelize} = require('sequelize')

const TABLE_NAME = 'tbl_product'

const ProductSchema = {
    id:{
        field:'id',
        allowNull:false,
        primaryKey:true,
        autoIncrement:true,
        type:DataTypes.INTEGER
    },
    name:{
        field:'name',
        allowNull:false,
        type:DataTypes.STRING
    },
    description:{
        field:'description',
        allowNull:true,
        type:DataTypes.STRING
    },
    price:{
        field:'price',
        allowNull:false,
        type:DataTypes.DOUBLE
    },
    image:{
        field:'image',
        allowNull:true,
        type:DataTypes.STRING
    },
    stock:{
        field:'stock',
        allowNull:true,
        type:DataTypes.INTEGER
    },
    categoryId:{
        field:'category_id',
        allowNull:false,
        type:DataTypes.INTEGER
    }
}

class Product extends Model{
    static config(sequelize){
        return {
            sequelize,
            tableName:TABLE_NAME,
            modelName:'Product',
            timestamps:false
        }
    }
}

module.exports = {TABLE_NAME,ProductSchema,Product}
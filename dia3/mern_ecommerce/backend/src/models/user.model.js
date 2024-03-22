const mongoose = require('mongoose')
const Schema = mongoose.Schema

const UserSchema = new Schema({
    email:{
        type:String,
        require:true,
        match: /.+\@.+\..+/,
    },
    password:{
        type:String,
        required:true,
    },
    isAdmin:{
        type:Boolean,
        default:false
    }
},{
    timestamps: false,
    versionKey:false
})

module.exports = mongoose.model('users',UserSchema)
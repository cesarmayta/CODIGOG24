const Joi = require('joi')

const name = Joi.string().min(3).max(200)

const CategorySchema = Joi.object({
    name : name.required()
})

module.exports = {CategorySchema}
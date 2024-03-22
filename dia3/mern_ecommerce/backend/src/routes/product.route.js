const {Router} = require('express')
const router = Router()

const {uploadImage} = require('../controllers/product.controller')

router.route('/upload')
    .post(uploadImage)

module.exports = router
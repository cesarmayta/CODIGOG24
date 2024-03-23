require('dotenv').config()

const config = {
    port : process.env.PORT || 5000,
    mongoUri: process.env.MONGOURI || 'mongodb://localhost:27017/db_ecommerce_g24',
    jwt_secret: process.env.JWT_SECRET || 'QWERTY123',
    cloudinary:{
        cloud_name: process.env.CLOUDINARY_CLOUD_NAME,
        api_key:process.env.CLOUDINARY_API_KEY,
        api_secret:process.env.CLOUDINARY_API_SECRET
    },
    mscatalog:{
        port:process.env.MSCATALOG_PORT || 5001
    },
    msusers:{
        port:process.env.MSUSERS_PORT || 5002
    }
}

module.exports = {config}
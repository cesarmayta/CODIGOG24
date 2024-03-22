const productController = {}
const {uploadCloudinaryImage} = require('../libs/cloudinary.lib')


productController.uploadImage = async(req,res)=>{
    fileImage = req.files.image
    let uploadPath = '../backend/media/' + fileImage.name

    await fileImage.mv(uploadPath,(err)=>{
        if(!err){
            uploadCloudinaryImage(uploadPath)
                .then((imagen_url)=>{
                    res.status(201).json({
                        imagen : imagen_url
                    })
                })
        }else{
            res.status(500).json({
                message:'error : ' + err.message
            })
        }
    })
}

module.exports = productController
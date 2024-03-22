const productController = {}


productController.uploadImage = async(req,res)=>{
    fileImage = req.files.image
    let uploadPath = '../backend/media/' + fileImage.name

    await fileImage.mv(uploadPath,(err)=>{
        if(!err){
            res.status(201).json({
                imagen : uploadPath
            })
        }else{
            res.status(500).json({
                message:'error : ' + err.message
            })
        }
    })
}

module.exports = productController
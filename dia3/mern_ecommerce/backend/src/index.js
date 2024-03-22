const app = require('./app')
require('./libs/mongoose.lib')

async function main(){
    await app.listen(app.get('port'))
    console.log('servidor activo http://127.0.0.1:'+app.get('port'))
}

main()
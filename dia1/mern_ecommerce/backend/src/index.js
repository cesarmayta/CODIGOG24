const app = require('./app')

async function main(){
    await app.listen(app.get('port'))
    console.log('servidor activo http://127.0.0.1:'+app.get('port'))
}

main()
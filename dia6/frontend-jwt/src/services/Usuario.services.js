import axios from 'axios'
import {API_URL} from '../lib/Enviroments'

class UsuarioServices{
    constructor(){
        this.endpoint = ''
        this.token = ''
    }

    login(data){
        return axios.post(API_URL+"/login",data)
        .then(res=>{
            return res.data;
        })
        .catch(error =>{
            console.log("error : ",error.message)
            return {
                status:false,
                message:'credenciales incorrectas'
            }
        })
    }
}
export default new UsuarioServices()
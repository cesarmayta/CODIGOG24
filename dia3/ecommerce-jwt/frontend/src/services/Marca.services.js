import axios from 'axios'
import { API_URL } from '../lib/Enviroments'

class MarcaService{
    constructor(){
        this.table_name = 'marca'
    }

    getAll(){
        return axios.get(API_URL+"/"+this.table_name)
        .then(res=>{
            return res.data.content;
        })
    }
}

export default new MarcaService();
import React from 'react';
import axios from 'axios';

class App extends React.Component{

    componentDidMount(){
      console.log('cargando tareas...');
      axios.get('http://localhost:5000/tarea')
      .then(res=>{
        console.log(res.data.content)
      }
      )
    }

    render(){
      return(
        <div>
          <h1>Lista de Tareas</h1>
        </div>
      )
    }
}

export default App;

import React from 'react';
import axios from 'axios';
import 'bootstrap/dist/css/bootstrap.min.css'
import {Container,Table,Form,Button} from 'react-bootstrap'

class App extends React.Component{

    constructor(props){
      super(props)
      this.state = ({
        tareas:[],
        descripcion:'',
        estado:'pendiente'
      })
      this.cambioDescripcion = this.cambioDescripcion.bind(this);
    }

    cambioDescripcion(e){
      console.log(e.target.value)
      this.setState({
        descripcion: e.target.value
      })
    }

    componentDidMount(){
      console.log('cargando tareas...');
      axios.get('http://localhost:5000/tarea')
      .then(res=>{
        console.log(res.data.content)
        this.setState({
          tareas : res.data.content
        })
      }
      )
    }

    render(){
      return(
        <div>
          <Container>
            <h1>Lista de Tareas</h1>
            <Form>
              <Form.Group className='mb-3'>
                <Form.Control type="text"
                value={this.state.descripcion}
                onChange={this.cambioDescripcion}
                />
              </Form.Group>
              <Button variant='primary' type='submit'>
                Agregar Tarea
              </Button>
            </Form>
            <Table striped bordered hover variant="dark">
              <thead>
                <tr>
                  <th>Id</th>
                  <th>Tarea</th>
                  <th>Estado</th>
                </tr>
              </thead>
              <tbody>
                {this.state.tareas.map((tarea,index)=>{
                  return(
                    <tr key={index}>
                      <td>{tarea.id}</td>
                      <td>{tarea.descripcion}</td>
                      <td>{tarea.estado}</td>
                    </tr>
                  )
                })}
              </tbody>
            </Table>
          </Container>
          
        </div>
      )
    }
}

export default App;

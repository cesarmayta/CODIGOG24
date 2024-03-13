import { useState,useEffect } from "react";
import 'bootstrap/dist/css/bootstrap.min.css';
import {Container,Row,Col,Card,Button,Table,Form} from 'react-bootstrap';
import axios from 'axios';

function App(){
  const [tareas,setTareas] = useState([]);
  const [nombre,setNombre] = useState('');
  const [estado,setEstado] = useState('pendiente');
  const [refresh,setRefresh] = useState(false);

  useEffect(()=>{
      axios.get('http://localhost:5000/tarea')
      .then(res=>{
        console.log(res.data.content);
        setTareas(res.data.content);
      })
      setRefresh(false)
  },[refresh])

  function agregarTarea(e){
    e.preventDefault();
    let data = {
      descripcion:nombre,
      estado:estado
    }

    axios.post('http://localhost:5000/tarea',data)
    .then(res=>{
      setRefresh(true)
      setNombre('');
    }).catch((error)=>{
      console.log(error.toString());
    })
  }

  return (
    <section className="vh-100">
      <Container className="container py-5 h-100">
        <Row className="row d-flex justify-content-center align-items-center h-100">
          <Col className="col col-lg-9 col-xl-7">
            <Card className="card rounded-3">
              <Card.Body className="card-body p-4">
                <h4 className="text-center my-3 pb-3">Lista de Tareas</h4>

                <Col className="col-12">
                  <Form onSubmit={agregarTarea}>
                    <div className="form-outline">
                      <input type="text" id="form1" className="form-control" onChange={(e)=>setNombre(e.target.value)} />
                    </div>
                    <div className="form-outline">
                      <Button type="submit" className="btn btn-primary">Agregar</Button>
                    </div>
                  </Form>
                </Col>

                <Table className="table mb-4">
                  <thead>
                    <tr>
                      <th scope="col">Tarea</th>
                      <th scope="col">Estado</th>
                    </tr>
                  </thead>
                  <tbody id="cuerpoTabla">
                  {tareas.map((tarea)=>{
                      return(
                        <tr key={0}>
                          <td>{tarea.descripcion}</td>
                          <td>{tarea.estado}</td>
                        </tr>
                      )
                  })}
                  </tbody>
                </Table>
              </Card.Body>
            </Card>
          </Col>
        </Row>
      </Container>
    </section>
  )
}

export default App
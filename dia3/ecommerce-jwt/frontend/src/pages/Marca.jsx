import {Container,Table} from 'react-bootstrap'
import MarcaServices from '../services/Marca.services'
import { useEffect, useState } from 'react'


const Marca = () => {
    const [data,setData] = useState([])

    useEffect(()=>{
        MarcaServices.getAll().then(
            (res)=>{
                setData(res);
            }
        )
    },[])

    return(
        <>
            <Container>
                <h1>Marcas</h1>
                <Table striped bordered hover variant="dark">
                    <thead>
                        <tr>
                        <th>Id</th>
                        <th>Nombre</th>
                        </tr>
                    </thead>
                    <tbody>
                        {data.map(dt=>{
                            return (
                                <tr key={dt.id}>
                                    <td>{dt.id}</td>
                                    <td>{dt.nombre}</td>
                                </tr>
                            )
                        })}
                    </tbody>
                </Table>
            </Container>
        </>
    )
}

export default Marca
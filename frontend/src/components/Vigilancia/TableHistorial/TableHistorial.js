import React from "react";
import {
  Form,
  Button,
  Select,
  Card,
  Image,
  List,
  Icon,
  ListContent,
} from "semantic-ui-react";
import { map } from "lodash";
import "./TableHistorial.scss";

export function TableHistorial(props) {
  const {onDeleteHistorial} = props
  const seguimientos = [
    {
      id_turno:1,
      fecha_turno: "02-02-2023",
      observaciones: "COVID",
      legajos: [
        {
          empleado:"2020",
          nombre:"Nicolas Yañez"
        },
        {
          empleado:"3030",
          nombre: "Jesus Escalante"
        }
      ],
    },
    {
      fecha_turno: "03-03-2023",
      tipo_seguimiento: 1,
      observaciones: "COVID",
      legajos: [
        {
          empleado:"2020",
          nombre:"Saul Jimenez"
        },{
          empleado:"3030",
          nombre:"Fabian Lopez"
        }
      ],
    },{
      fecha_turno: "02-02-2023",
      tipo_seguimiento: 1,
      observaciones: "COVID",
      legajos: [
        {
          empleado:"2020",
          nombre:"Nicolas Yañez"
        },
        {
          empleado:"3030",
          nombre: "Jesus Escalante"
        }
      ],
    },
    {
      fecha_turno: "03-03-2023",
      tipo_seguimiento: 1,
      observaciones: "COVID",
      legajos: [
        {
          empleado:"2020",
          nombre:"Saul Jimenez"
        },{
          empleado:"3030",
          nombre:"Fabian Lopez"
        },{
          empleado:"2333",
          nombre:"SAC Jimenez"
        },{
          empleado:"1111",
          nombre:"SES Lopez"
        }
      ],
    },
    {
      fecha_turno: "02-02-2023",
      tipo_seguimiento: 1,
      observaciones: "COVID",
      legajos: [
        {
          empleado:"2020",
          nombre:"Nicolas Yañez"
        },
        {
          empleado:"3030",
          nombre: "Jesus Escalante"
        }
      ],
    },
    {
      fecha_turno: "03-03-2023",
      tipo_seguimiento: 1,
      observaciones: "COVID",
      legajos: [
        {
          empleado:"2020",
          nombre:"Saul Jimenez"
        },{
          empleado:"3030",
          nombre:"Fabian Lopez"
        }
      ],
    },
  ];
  return (
    <>
      {seguimientos.length !== 0 ? ( 
        <Card.Group className="custom-card-group">
          {map(seguimientos, (seguimiento, index) => {
            return (
              <Card className="custom-card-group-card" key={index}>
                <div className="delete-button">
                <Button icon negative onClick={()=>onDeleteHistorial()} >
                    <Icon name="close" />
                  </Button>
                  </div>
                <Card.Content className="centered-content">
                  <div className="icon-container">
                    <Icon name="shield" size="huge" color="blue" />
                  </div>
                  <Card.Header>Fecha : {seguimiento.fecha_turno}</Card.Header>
                  <Card.Meta>Legajos de Personal Afectado</Card.Meta>
                  <Card.Description>
                  <Card.Description className="legajos">
                    <List >
                      {seguimiento.legajos?.map((legajos, index) => {
                        return (
                          <List.Item key={index} >
                            <List.Icon name="dot circle" color="blue" />
                            <List.Content className="lista-personal-contenido">Legajo: {legajos.empleado} </List.Content>
                            <ListContent className="lista-personal-contenido"> Nombre: {legajos.nombre}</ListContent>
                          </List.Item>
                        );
                      })}
                    </List>
                  </Card.Description>
                  </Card.Description>
                </Card.Content>
                <Card.Content extra>
                  <Icon name="user" /> 
                  {seguimiento.legajos.length} Personales afectados a este turno
                </Card.Content>
              </Card>
            );
          })}
        </Card.Group>
      ) : (
        <>
          <div className="no-seguimiento">
          <h1>Aún no inicio la asignacion del personal</h1>
          </div>
        </>
      )}
    </>
  );
}

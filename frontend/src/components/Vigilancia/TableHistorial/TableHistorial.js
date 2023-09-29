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
import { useVigilancia } from "../../../hooks/";
import { map } from "lodash";
import { useEffect } from "react";
import "./TableHistorial.scss";

export function TableHistorial(props) {
  const { onDeleteHistorial, id } = props;
  const { get_turnos, historial } = useVigilancia();
  useEffect(() => {
    get_turnos(id);
  }, []);
  return (
    <>
    {/* Buscar la secccion desde se cargan los legajos de los personales afectados */}
      {historial && historial?.length !== 0 ? (
        <Card.Group className="custom-card-group">
          {Array.from(historial)
            .reverse()
            .map((seguimiento, index) => {
              return (
                <Card className="custom-card-group-card" key={index}>
                  <div className="delete-button">
                    <Button
                      icon
                      negative
                      onClick={() => onDeleteHistorial(id, seguimiento[0].id)}
                    >
                      <Icon name="close" />
                    </Button>
                  </div>
                  <Card.Content className="centered-content">
                    <div className="icon-container">
                      <Icon name="shield" size="huge" color="blue" />
                    </div>
                    <Card.Header>Fecha : {seguimiento[0].fecha}</Card.Header>
                    <Card.Meta>Legajos de Personal Afectado</Card.Meta>
                    <Card.Description>
                      <Card.Description className="legajos">
                        <List>
                          {seguimiento[0].personal?.map((legajos, index) => {
                            return (
                              <List.Item key={index}>
                                <List.Icon name="dot circle" color="blue" />
                                <List.Content className="lista-personal-contenido">
                                  Legajo: {legajos.legajo}{" "}
                                </List.Content>
                                <ListContent className="lista-personal-contenido">
                                  {" "}
                                  Nombre: {legajos.nombre}
                                </ListContent>
                              </List.Item>
                            );
                          })}
                        </List>
                      </Card.Description>
                    </Card.Description>
                  </Card.Content>
                  <Card.Content extra>
                    <Icon name="user" />
                    {seguimiento[0].personal?.length} Personales afectados a este
                    turno
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

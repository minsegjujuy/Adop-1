import React, { useState } from "react";
import { Table, Button, Icon} from "semantic-ui-react";
import { Link } from "react-router-dom";
import { map } from "lodash";
import "./TableVigilancia.scss";

export function TableVigilancia(props) {
  const { vigilancias, addHorarios, vermapa} = props;
  const { position, setposition } = useState(null);

  return (
    <Table className="table-users-admin">
      <Table.Header>
        <Table.Row>
          <Table.HeaderCell>Regional</Table.HeaderCell>
          <Table.HeaderCell>Comisaria</Table.HeaderCell>
          <Table.HeaderCell>Motivo</Table.HeaderCell>
          <Table.HeaderCell>Tipo de Servicio</Table.HeaderCell>
          <Table.HeaderCell>Objetivo</Table.HeaderCell>
          {/* <Table.HeaderCell>Dias</Table.HeaderCell> */}
          <Table.HeaderCell>Fecha de inicio</Table.HeaderCell>
          <Table.HeaderCell>Fecha de fin</Table.HeaderCell>
          {/* <Table.HeaderCell>Latitud</Table.HeaderCell>
          <Table.HeaderCell>Longitud</Table.HeaderCell> */}

          <Table.HeaderCell></Table.HeaderCell>
        </Table.Row>
      </Table.Header>
      <Table.Body>
        {map(vigilancias, (vigilancia, index) => (
          <Table.Row key={index}>
            <Table.Cell>{vigilancia.fk_unidad_regional}</Table.Cell>
            <Table.Cell>{vigilancia.jurisdiccion}</Table.Cell>
            <Table.Cell>{vigilancia.motivo}</Table.Cell>
            <Table.Cell>{vigilancia.servicio}</Table.Cell>
            <Table.Cell>{vigilancia.objetivo}</Table.Cell>
            {/* <Table.Cell>{vigilancia.cant_dias}</Table.Cell> */}
            <Table.Cell>{vigilancia.fecha_inicio.slice(0, 10)}</Table.Cell>
            <Table.Cell>
              {vigilancia.fecha_fin
                ? vigilancia.fecha_fin.slice(0, 10)
                : "indefinida"}
            </Table.Cell>
            {/* <Table.Cell>{vigilancia.latitud}</Table.Cell>
            <Table.Cell>{vigilancia.longitud}</Table.Cell> */}

            <Actions
              // user={user}
              addHorarios={addHorarios}
              vermapa={vermapa}
              fecha_inicio={vigilancia.fecha_inicio.slice(0, 10)}
              fecha_fin={
                vigilancia.fecha_fin ? vigilancia.fecha_fin.slice(0, 10) : null
              }
              jurisdiccion={vigilancia.jurisdiccion}
              servicio={vigilancia.servicio}
              latitud={vigilancia.latitud}
              longitud={vigilancia.longitud}
              position={position}
              setposition={setposition}
              id={vigilancia.id}
              turno_asignado={vigilancia.turno_asignado}
              //   updateUser={updateUser}
              //  onDeleteUser={onDeleteUser}
            />
          </Table.Row>
        ))}
      </Table.Body>
    </Table>
  );
}

function Actions(props) {
  const {
    addHorarios,
    fecha_fin,
    fecha_inicio,
    latitud,
    longitud,
    vermapa,
    id,
    turno_asignado,
    jurisdiccion,
   servicio,
  } = props;
  const position = {
    lat: latitud,
    lng: longitud,
  };

  return (
    <Table.Cell textAlign="right">
     {turno_asignado===false && (
      <Button
        positive
        icon
        onClick={() => addHorarios(fecha_fin, fecha_inicio, id)}
      >
        {/* <Icon className="green" name="pencil" /> */}
        Turnos
      </Button>
      )}
      {turno_asignado===true && (
      <Link
        to="/admin/carga/vigilancia/personal"
        state={{ fecha_fin,fecha_inicio,jurisdiccion,servicio }}
      >
         
        <Button positive>
        <Icon className="user icon"/>
          Asignar Personal</Button>
      </Link>
)}
      <Button icon onClick={() => vermapa(position, true)}>
        <Icon name="map marker" />
      </Button>

      <Button icon negative onClick={() => console.log("hola mundo")}>
        <Icon title="ver mapa" name="close" />
      </Button>
    </Table.Cell>
  );
}

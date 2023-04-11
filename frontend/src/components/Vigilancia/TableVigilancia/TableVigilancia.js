import React from "react";
import { Table, Button, Icon } from "semantic-ui-react";
import { map } from "lodash";
import "./TableVigilancia.scss";


export function TableVigilancia(props) {
  const {vigilancias,addHorarios } = props;
 
  return (
    <Table className="table-users-admin">
      <Table.Header>
        <Table.Row>
          <Table.HeaderCell>Regional</Table.HeaderCell>
          <Table.HeaderCell>Comisaria</Table.HeaderCell>
          <Table.HeaderCell>Motivo</Table.HeaderCell>
          <Table.HeaderCell>Tipo de Servicio</Table.HeaderCell>
          <Table.HeaderCell>Objetivo</Table.HeaderCell>
          <Table.HeaderCell>Dias</Table.HeaderCell>
          <Table.HeaderCell>Fecha de inicio</Table.HeaderCell>
          <Table.HeaderCell>Fecha de fin</Table.HeaderCell>
          <Table.HeaderCell>Latitud</Table.HeaderCell>
          <Table.HeaderCell>Longitud</Table.HeaderCell>

          <Table.HeaderCell></Table.HeaderCell>
        </Table.Row>
      </Table.Header>
      <Table.Body>
        {map(vigilancias, (vigilancia, index) => (
          <Table.Row
            key={index}

          > 
             <Table.Cell>{vigilancia.regional}</Table.Cell>
            <Table.Cell>{vigilancia.jurisdiccion}</Table.Cell>
            <Table.Cell>{vigilancia.motivo}</Table.Cell>
            <Table.Cell>{vigilancia.servicio}</Table.Cell>
            <Table.Cell>{vigilancia.objetivo}</Table.Cell>
            <Table.Cell>{vigilancia.cant_dias}</Table.Cell>
            <Table.Cell>{vigilancia.fecha_inicio.slice(0, 10)}</Table.Cell>
            <Table.Cell>{vigilancia.fecha_fin? vigilancia.fecha_fin.slice(0,10):"indefinida"}</Table.Cell>
            <Table.Cell>{vigilancia.latitud}</Table.Cell>
            <Table.Cell>{vigilancia.longitud}</Table.Cell>
            
            <Actions
              // user={user}
               addHorarios={addHorarios}
               fecha_fin={vigilancia.fecha_fin.slice(0,10)}
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
  const { addHorarios,fecha_fin} = props;
  return (
    <Table.Cell textAlign="right">
            
      <Button positive icon onClick={() => addHorarios(fecha_fin)}>
        {/* <Icon className="green" name="pencil" /> */}
        Turnos
      </Button>

      <Button icon negative onClick={()=>console.log("hola mundo")}>
        <Icon name="close" />
      </Button>
    </Table.Cell>
  );
}

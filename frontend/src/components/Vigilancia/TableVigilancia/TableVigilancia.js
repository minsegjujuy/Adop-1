import React from "react";
import { Table, Button, Icon } from "semantic-ui-react";
import { map } from "lodash";
import "./TableVigilancia.scss";


export function TableVigilancia(props) {
//   const { } = props;
 
  return (
    <Table className="table-users-admin">
      <Table.Header>
        <Table.Row>
          <Table.HeaderCell>Id Vigilancia</Table.HeaderCell>
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
      {/* <Table.Body>
        {map(users, (user, index) => (
          <Table.Row
            key={index}

          >
            <Table.Cell>{user.User.username}</Table.Cell>
            <Table.Cell>{user.User.email}</Table.Cell>
            <Table.Cell>{user.User.first_name}</Table.Cell>
            <Table.Cell>{user.User.last_name}</Table.Cell>
            <Table.Cell className="status">
              {user?.User.is_active ? (
                <Icon name="check" />
              ) : (
                <Icon name="close" />
              )}
            </Table.Cell>
            <Table.Cell className="status">
              {user?.User.is_staff ? (
                <Icon name="check" />
              ) : (
                <Icon name="close" />
              )}
            </Table.Cell>
            <Table.Cell>{user.nivel_permiso}</Table.Cell>
            <Actions
              user={user}
            //   updateUser={updateUser}
               onDeleteUser={onDeleteUser}
              
            />
          </Table.Row>
        ))}
      </Table.Body> */}
    </Table>
  );
}

function Actions(props) {
  const { user, updateUser, onDeleteUser } = props;
  return (
    <Table.Cell textAlign="right">
            
      <Button icon onClick={() => updateUser(user,"contra")}>
        <Icon name="pencil" />
      </Button>

      <Button icon negative onClick={() => onDeleteUser(user)}>
        <Icon name="close" />
      </Button>
    </Table.Cell>
  );
}

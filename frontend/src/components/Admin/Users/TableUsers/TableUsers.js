import React from "react";
import { Table, Button, Icon } from "semantic-ui-react";
import { map } from "lodash";
import "./TableUsers.scss";


export function TableUsers(props) {
  const {users,onDeleteUser} = props;  

  console.log(users)
  return (
    <Table className="table-users-admin">
      <Table.Header>
        <Table.Row>
          <Table.HeaderCell>Username</Table.HeaderCell>
          <Table.HeaderCell>Email</Table.HeaderCell>
          <Table.HeaderCell>Nombre</Table.HeaderCell>
          <Table.HeaderCell>Apellido</Table.HeaderCell>
          <Table.HeaderCell>Activo</Table.HeaderCell>
          <Table.HeaderCell>Staff</Table.HeaderCell>
          <Table.HeaderCell>Tipo de Permiso</Table.HeaderCell>
          <Table.HeaderCell>Regional</Table.HeaderCell>
          <Table.HeaderCell>Jurisdiccion</Table.HeaderCell>
          
          <Table.HeaderCell></Table.HeaderCell>
        </Table.Row>
      </Table.Header>
      <Table.Body>
        {map(users, (user, index) => (
          <Table.Row
            key={index}

          >
            <Table.Cell>{user.username}</Table.Cell>
            <Table.Cell>{user.email}</Table.Cell>
            <Table.Cell>{user.nombres}</Table.Cell>
            <Table.Cell>{user.apellidos}</Table.Cell>
            <Table.Cell className="status">
              {user?.usuario_activo ? (
                <Icon name="check" />
              ) : (
                <Icon name="close" />
              )}
            </Table.Cell>
            <Table.Cell className="status">
              {user?.is_superuser ? (
                <Icon name="check" />
              ) : (
                <Icon name="close" />
              )}
            </Table.Cell>
            <Table.Cell>{user.rol}</Table.Cell>
            <Table.Cell>{user.unidad_regional}</Table.Cell>
            <Table.Cell>{user.jurisdiccion}</Table.Cell>
            <Actions
              user={user}
            //   updateUser={updateUser}
               onDeleteUser={onDeleteUser}
              
            />
          </Table.Row>
        ))}
      </Table.Body>
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

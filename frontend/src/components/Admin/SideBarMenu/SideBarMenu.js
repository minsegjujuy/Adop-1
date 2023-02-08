import React from "react";
import "./SideBarMenu.scss";
import { Menu, Icon } from "semantic-ui-react";
import { Link, useLocation } from "react-router-dom";
import { useAuth } from "../../../hooks/useAuth";
import { useState, useEffect } from "react";

export function SideBarMenu(props) {
  const { children} = props;
  const { pathname } = useLocation();

  return (
    <div className="side-menu-admin">
      <MenuLeft pathname={pathname} />
      <div className="contentenido">{children}</div>
    </div>
  );
}

function MenuLeft(props) {
  const { pathname } = props;
  const { auth } = useAuth();
  //const [empleados, setEmpleado] = useState(false);
//   useEffect(() => {
//     Permiso();
//   }, []);

//   const Permiso = async () => {
//     const empleado = await buscarEmpleadoId(auth?.me.id);

//     if (empleado[0].nivel_permiso === "farmaceutico") {
//       setEmpleado(true);
//     }
//   };
  return (
    <Menu fixed="left" borderless className="side" vertical>
      {/* <Menu.Item as={Link} to={"/admin"} active={pathname === "/admin"}>
        <Icon name="home" className="icono-side-bar" />
        Home
      </Menu.Item> */}

      {/* <Menu.Item
        as={Link}
        to={"/admin/tables"}
        active={pathname === "/admin/tables"}
      >
        <Icon name="table" className="icono-side-bar" />
        Pacientes
      </Menu.Item> */}

      {/* {empleados === true && (
        <Menu.Item
          as={Link}
          to={"/admin/farmaceutico"}
          active={pathname === "/admin/farmaceutico"}
        >
          <Icon name="hospital" className="icono-side-bar" />
          Pacientes
        </Menu.Item>
      )} */}

      {/* {empleados === false && (
        <Menu.Item
          as={Link}
          to={"/admin/diabetes"}
          active={pathname === "/admin/diabetes"}
        >
          <Icon name="hospital" className="icono-side-bar" />
          Pacientes-Diabetes
        </Menu.Item>
      )}

      {empleados === false && (
        <Menu.Item
          as={Link}
          to={"/admin/pacientes"}
          active={pathname === "/admin/pacientes"}
        >
          <Icon name="emergency" className="icono-side-bar" />
          Pacientes
        </Menu.Item>
      )} */}

      <Menu.Item
        as={Link}
        to={"/admin/contrasena"}
        active={pathname === "/admin/contrasena"}
      >
      <Icon name="pencil alternate" className="icono-side-bar" />
        Gestion de Contraseña
      </Menu.Item>

      {auth?.me?.is_staff && (
        <Menu.Item
          as={Link}
          to={"/admin/users"}
          active={pathname === "/admin/users"}
        >
        <Icon name="user" className="icono-side-bar" />
          Usuarios
        </Menu.Item>
      )}
    </Menu>
  );
}

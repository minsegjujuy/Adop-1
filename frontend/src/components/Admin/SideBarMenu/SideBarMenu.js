import React from "react";
import "./SideBarMenu.scss";
import { Menu, Icon } from "semantic-ui-react";
import { Link, useLocation } from "react-router-dom";
import { useAuth } from "../../../hooks/useAuth";
import {useUser} from "../../../hooks"
import { useState, useEffect } from "react";

export function SideBarMenu(props) {
  const { children} = props;
  const { pathname } = useLocation();


  return (
    <div className="side-menu-admin">
      <MenuLeft pathname={pathname} />
      <div className="contenido">{children}</div>
    </div>
  );
}

function MenuLeft(props) {
  const { pathname } = props;
  const { auth } =  useAuth();
  // const {buscarEmpleadoId} = useUser()
  // const [empleados, setEmpleado] = useState(null);
  useEffect(() => {
    // Permiso();
  }, []);

  const Permiso = async () => {
    // const response = await buscarEmpleadoId(auth?.me.id);
    // console.log(response)
    // if (response[0].nivel_permiso === "operador") {
    //   setEmpleado("operador");
    // }
    // if (response[0].nivel_permiso === "general") {
    //   setEmpleado("gemeral");
    // }
    // if (response[0].nivel_permiso === "administrador") {
    //   setEmpleado("administrador");
    // }
  };
// console.log(empleados)
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

      {auth?.usuario?.rol ==="operador" && (
        <Menu.Item
          as={Link}
          to={"/admin/farmaceutico"}
          active={pathname === "/admin/farmaceutico"}
        >
          <Icon name="hospital" className="icono-side-bar" />
          Pacientes
        </Menu.Item>
      )}
      
      {(auth?.usuario?.rol==="administrador") && (
        <Menu.Item
          as={Link}
          to={"/admin/vigilancia"}
          active={pathname === "/admin/vigilancia"}
        >
        <Icon name="hospital" className="icono-side-bar"/>
          Vigilancia
        </Menu.Item>
      )}
      
      {/* {empleados = && (
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

      {auth?.usuario?.rol==="administrador" && (
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

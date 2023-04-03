import React from "react";
import "./SideBarMenu.scss";
import { Menu, Icon, Select, Dropdown } from "semantic-ui-react";
import { Link, useLocation } from "react-router-dom";
import { useAuth } from "../../../hooks/useAuth";
import { useUser } from "../../../hooks";
import { useState, useEffect } from "react";

export function SideBarMenu(props) {
  const { children } = props;
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
  const { auth } = useAuth();
  const [mostrar, setMostrar] = useState(null);
  // const {buscarEmpleadoId} = useUser()
  // const [empleados, setEmpleado] = useState(null);
  // console.log(empleados)
  const options = [
    { key: "1", text: "Tabla 1", value: "Tabla 1" },
    { key: "2", text: "Tabla 2", value: "Tabla 2" },
    { key: "3", text: "Tabla 3", value: "Tabla 3" },
  ];
  return (
    <Menu fixed="left" borderless class="side" vertical>
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

      {auth?.usuario?.rol === "operador" && (
        <Menu.Item
          as={Link}
          to={"/admin/farmaceutico"}
          active={pathname === "/admin/farmaceutico"}
        >
          <Icon name="hospital" className="icono-side-bar" />
          Pacientes
        </Menu.Item>
      )}

      {auth?.usuario?.rol === "administrador" && (
        <Menu.Item
          as={Link}
          to={"/admin/vigilancia"}
          active={pathname === "/admin/vigilancia"}
        >
          <Icon name="hospital" className="icono-side-bar" />
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
      <Menu.Item>
        <div className="header_class">
          <Icon name="chart bar" className="icono-side-bar" />
          <Dropdown item text="Tableros">
            <Dropdown.Menu>
              <Dropdown.Item
                as={Link}
                to={"/admin/tableros"}
                active={pathname === "/admin/tableros"}
              >
                Tablero 1
              </Dropdown.Item>
              <Dropdown.Item
                as={Link}
                to={"/admin/tableros"}
                active={pathname === "/admin/tableros"}
              >
                Tablero 2
              </Dropdown.Item>
              <Dropdown.Item
                as={Link}
                to={"/admin/tableros"}
                active={pathname === "/admin/tableros"}
              >
                Tablero 3
              </Dropdown.Item>
            </Dropdown.Menu>
          </Dropdown>
        </div>
        {/* <div class="ui dropdown item"><i class="dropdown icon"></i> Opciones de visualización 
       <div class="menu">
       <div class="header">Tamaño de texto</div>
       <a class="item">Pequeño</a>
       <a class="item">Mediano</a>
       <a class="item">Grande</a>
     </div>
      */}
      </Menu.Item>

      {auth?.usuario?.rol === "administrador" && (
        <Menu.Item
          as={Link}
          to={"/admin/users"}
          active={pathname === "/admin/users"}
        >
          <Icon name="user" className="icono-side-bar" />
          Usuarios
        </Menu.Item>
      )}
      <Menu.Item
        as={Link}
        to={"/admin/contrasena"}
        active={pathname === "/admin/contrasena"}
      >
        <Icon name="pencil alternate" className="icono-side-bar" />
        Gestion de Contraseña
      </Menu.Item>
    </Menu>
  );
}

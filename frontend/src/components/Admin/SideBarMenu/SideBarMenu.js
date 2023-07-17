import React from "react";
import "./SideBarMenu.scss";
import { Menu, Icon, Dropdown } from "semantic-ui-react";
import { Link, useLocation } from "react-router-dom";
import { useAuth } from "../../../hooks/useAuth";

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
  // const {buscarEmpleadoId} = useUser()
  // const [empleados, setEmpleado] = useState(null);
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

      {/* {auth?.usuario?.rol === "operador" && (
        <Menu.Item
          as={Link}
          to={"/admin/farmaceutico"}
          active={pathname === "/admin/farmaceutico"}
        >
          <Icon name="hospital" className="icono-side-bar" />
          Pacientes
        </Menu.Item>
      )} */}

      {((auth?.usuario?.rol === 1) || (auth?.usuario?.rol ===3)) && (
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
      <Menu.Item className="header_class">
        
          <Icon name="chart bar" className="icono-side-bar" />
          <Dropdown item text="Tableros">
            <Dropdown.Menu>
              <Dropdown.Item
                as={Link}
                to={"/admin/tableros/escuelas"}
                active={pathname === "/admin/tableros/escuelas"}
              >
                Vigilancia y escuelas
              </Dropdown.Item>
              <Dropdown.Item
                as={Link}
                to={"/admin/tableros/propiedad"}
                active={pathname === "/admin/tableros/propiedad"}
              >
                Analisis Propiedad 2022
              </Dropdown.Item>
              <Dropdown.Item
                as={Link}
                to={"/admin/tableros/contravencion"}
                active={pathname === "/admin/tableros/contravencion"}
              >
                Contravencion General
              </Dropdown.Item>
              <Dropdown.Item
                as={Link}
                to={"/admin/tableros/violencia"}
                active={pathname === "/admin/tableros/violencia"}
              >
                Violencia
              </Dropdown.Item>
            </Dropdown.Menu>
          </Dropdown>
        
      
      </Menu.Item>

      {auth?.usuario?.rol === 1 && (
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

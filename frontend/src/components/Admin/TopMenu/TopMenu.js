import React from "react";
import "./TopMenu.scss";
import { Icon, Menu } from "semantic-ui-react";
import { useAuth } from "../../../hooks/";

export function TopMenu() {
  const { auth, logout } = useAuth();

  const renderName = () => {
    if (auth?.usaurio?.nombres && auth?.usuario?.apellidos) {
      return `${auth.usuario.nombres} ${auth.usuario.apellidos}`;
    }
    // console.log(auth)
    return auth?.usuario?.email;
  };

  return (
    <Menu fixed="top" className="top-menu-admin">
      <Menu.Item className="top-menu-admin__logo">
        <p>SISTEMA DE VIGILANCIA</p>
      </Menu.Item>

      <Menu.Menu position="right">
        <Menu.Item>
          <p style={{ color: "black" }}> Bienvenido , {renderName()}</p>
        </Menu.Item>
        <Menu.Item onClick={logout}>
          <Icon name="sign-out"></Icon>
        </Menu.Item>
      </Menu.Menu>
    </Menu>
  );
}

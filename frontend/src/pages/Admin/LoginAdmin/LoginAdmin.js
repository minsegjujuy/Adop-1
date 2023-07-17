import React, { useEffect, useState } from "react";
import { LoginForm, Footer } from "../../../components/Admin";
import { Modal, Button, Icon } from "semantic-ui-react";
import { logoutApi } from "../../../api/user";
import { useAuth } from "../../../hooks";
import { removeToken } from "../../../api/token";
// import { ModalRecuperarContrasenia } from "../../../components/Common";
// import { RecuperarContrasenia } from "../../../components/Admin";
import "./LoginAdmin.scss";

export function LoginAdmin(props) {
  const { logueo, setLogueo } = props;
  const { auth, setAuth } = useAuth();
  useEffect(() => {
    if (logueo === false) {
      removeToken();
      setAuth(null);
      logoutApi(auth.token);
      setLogueo(true);
    }
  }, []);

  // window.location.replace("http://localhost:3000/login")

  return (
    <div className="Area">
      <div className="title-ministerio">
        <h1>
          <img
            className="img-ministerio"
            src="img/LOGO2.png"
            height="140px"
            width="510px"
            alt="SISTEMA DE VIGILANCIA"
          />
        </h1>
      </div>
      <div className="login-admin">
        <div className="login-admin__content">
          <h1 className="titulo-onda">INICIO DE SESION</h1>
          <LoginForm />
          <div className="recuperar-contraseña-usuario">
            <span style={{ fontWeight: "bold", fontSize: "16px" }}>
              ¿OLVIDO SU CONTRASEÑA?
            </span>
            <Button
              className="login-button"
              icon
              primary
              onClick={() => console.log("hola munbdo")}
            >
              RECUPERAR CONTRASEÑA
            </Button>
            {/* // <Button icon primary onClick={console.log("hola munbdo")}>
            //   RECUPERAR CONTRASEÑA
            // </Button> */}
          </div>
        </div>
      </div>
      <div className="footer">
      <Footer/>
      </div> 
        
      
      <div>
        <ul className="circles">
          <li></li>
          <li></li>
          <li></li>
          <li></li>
          <li></li>
          <li></li>
          <li></li>
          <li></li>
          <li></li>
          <li></li>
        </ul>
      </div>
     
    </div>
  );
}

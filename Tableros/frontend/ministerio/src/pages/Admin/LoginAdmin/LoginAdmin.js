import React, { useState } from "react";
import { LoginForm } from "../../../components/Admin";
import { Modal, Button, Icon } from "semantic-ui-react";
// import { ModalRecuperarContrasenia } from "../../../components/Common";
// import { RecuperarContrasenia } from "../../../components/Admin";
import "./LoginAdmin.scss";

export function LoginAdmin() {
//   const [
//     contentModalRecuperarContrasenia,
//     setContentModalRecuperarContrasenia,
//   ] = useState(false);
//   const [showModalRecuperarContrasenia, setShowModalRecuperarContrasenia] =
//     useState(false);
//   const openCloseModalRecuperarContrasenia = () => {
//     setShowModalRecuperarContrasenia((prev) => !prev);
//   };

//   const RecuperarContraseniaFuncion = () => {
//     setContentModalRecuperarContrasenia(
//       <RecuperarContrasenia onClose={openCloseModalRecuperarContrasenia} />
//     );
//     openCloseModalRecuperarContrasenia();
//   };

  return (
    <>
        {/* <div className="title-ministerio">
        <h1>OBSERVATORIO DE SEGURIDAD</h1>
        <div className="title-ministerio__logo"></div>
        <img 
            className="img-ministerio"
            src="img/LOGO2.png"
            height="150px"
            width="100px"
            alt="SISTEMA DE SANIDAD"
          />
        </div> */}
      <div className="title-ministerio">
      <h1><img 
            className="img-ministerio"
            src="img/LOGO2.png"
            height="140px"
            width="510px"
            alt="SISTEMA DE SANIDAD"
          /></h1>
      </div>
      <div className="login-admin">
        <div className="login-admin__content">
          <h1>INICIO DE SESION</h1>
          <LoginForm />
          <div className="recuperar-contraseña-usuario">
            <span style={{ fontWeight: "bold", fontSize: "16px" }}>
              ¿OLVIDO SU CONTRASEÑA?
            </span>
            <Button icon primary onClick={()=>console.log("hola munbdo")} >RECUPERAR CONTRASEÑA</Button>
            {/* // <Button icon primary onClick={console.log("hola munbdo")}>
            //   RECUPERAR CONTRASEÑA
            // </Button> */}
          </div>
        </div>
      </div>

      {/* <ModalRecuperarContrasenia
        show={showModalRecuperarContrasenia}
        title={"Recuperar contraseña"}
        children={contentModalRecuperarContrasenia}
        onClose={openCloseModalRecuperarContrasenia}
      /> */}
      
    </>
  );
}

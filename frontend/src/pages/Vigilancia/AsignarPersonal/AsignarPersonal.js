import React from "react";
import { HeaderPage } from "../../../components/Admin";
import { CargaPersonal } from "../../../components/Vigilancia/";
import { useAuth } from "../../../hooks";
import "./AsignarPersonal.scss";
// import Swal from "sweetalert2";
import { useLocation } from "react-router-dom";
export function AsignarPersonal(props) {
  const location = useLocation();
  console.log(location);
  const { fecha_fin, fecha_inicio } = location.state || {};
  console.log(fecha_fin, fecha_inicio);
  const { auth } = useAuth();

  return (
    <>
      <HeaderPage
        title="ASIGNAR PERSONAL"
        regional={
          auth.usuario.unidad_regional ? auth.usuario.unidad_regional : null
        }
      />
      <div className="form-vigilancia">
        <CargaPersonal fecha_fin={fecha_fin} fecha_inicio={fecha_inicio} />
      </div>
    </>
  );
}

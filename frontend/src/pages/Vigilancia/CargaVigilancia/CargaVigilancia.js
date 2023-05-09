import React from "react";
import { HeaderPage } from "../../../components/Admin";
import { AddVigilancia } from "../../../components/Vigilancia/CargaVigilancia";
import { useAuth } from "../../../hooks";
import "./CargaVigilancia.scss";

export function CargaVigilancia() {
  const { auth } = useAuth();
  console.log(document.referrer)
  return (
    <>
      <HeaderPage
        title="CARGA DE VIGILANCIA"
        regional={
          auth.usuario.unidad_regional ? auth.usuario.unidad_regional : null
        }
      />
      <div className="form-vigilancia">
        <AddVigilancia />
      </div>
    </>
  );
}

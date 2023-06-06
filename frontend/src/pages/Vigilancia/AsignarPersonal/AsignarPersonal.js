import React from "react";
import { HeaderPage } from "../../../components/Admin";
import { CargaPersonal } from "../../../components/Vigilancia/";
import {Personal} from "../../../components/Vigilancia/Personal"
import { useAuth } from "../../../hooks"
import { useState } from "react";
import "./AsignarPersonal.scss";
import {ModalBasic} from "../../../components/Common/ModalBasic"
// import Swal from "sweetalert2";
import { useLocation } from "react-router-dom";
export function AsignarPersonal(props) {
  const location = useLocation();
  const [titleModal, setTitleModal] = useState(null);
  const [showModal, setShowModal] = useState(false);
  const [contentModal, setContentModal] = useState(null);
  const [refetch, setRefetch] = useState(false);
  const { fecha_fin, fecha_inicio,jurisdiccion,servicio,id} = location.state || {};
 
  const { auth } = useAuth();
  const openCloseModal = () => {
    setShowModal((prev) => !prev);
  };
  const onRefetch = () => setRefetch((prev) => !prev);
  const addTurnos = (turno,duracion) => {
    setTitleModal("Asignar Personal");
   
    setContentModal(
      <Personal
      turnos={turno}
      duracion={duracion}
      />
    );
    openCloseModal();
  };
  return (
    <>
      <HeaderPage
        title="ASIGNAR PERSONAL"
        regional={
          auth.usuario.unidad_regional ? auth.usuario.unidad_regional : null
        }
      />
      <div className="form-vigilancia">
        <CargaPersonal fecha_fin={fecha_fin} fecha_inicio={fecha_inicio} jurisdiccion={jurisdiccion} servicio={servicio} id={id}
        addTurnos={addTurnos}/>
      </div>
      <ModalBasic
        show={showModal}
        title={titleModal}
        children={contentModal}
        onClose={openCloseModal}
        refetch={refetch}
      />
    </>
  );
}

import React from "react";
import { HeaderPage } from "../../../components/Admin";
import { CargaPersonal,TableHistorial } from "../../../components/Vigilancia/";
import {Personal} from "../../../components/Vigilancia/Personal"
import { useAuth } from "../../../hooks"
import { useState } from "react";
import "./AsignarPersonal.scss";
import {ModalBasic} from "../../../components/Common/ModalBasic"
import Swal from "sweetalert2";
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
  const addTurnos = (turno,duracion,id) => {
    setTitleModal("Asignar Personal");
   
    setContentModal(
      <Personal
      turnos={turno}
      duracion={duracion}
      id={id}
      />
    );
    openCloseModal();
  };
  const onDeleteHistorial= async (id) => {
    try {
      Swal.fire({
        icon: "question",
        iconColor: "lightblue",
        title: "Eliminar Historial",
        text: "¿Estas seguro que quieres eliminar este turno?",
        showCancelButton: true,
        showConfirmButton: true,
        confirmButtonText: "confirmar",
        cancelButtonText: "cancelar",
        reverseButtons: true,
        confirmButtonColor: "#3085d6",
        cancelButtonColor: "#d33",
      }).then(async (result) => {
        if (result.isConfirmed) {
          // await deleteUser(data.id);
          console.log("hola mundo")
          window.location.reload()
          // setUsers(null);

          Swal.fire({
            title: "Turno Eliminado!",
            text: "El turno fue eliminado",
            icon: "success",
            showConfirmButton: true,
            timer: 3000,
          });
        }
      });
    } catch (error) {
      console.error(error);
    }
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
        <CargaPersonal jurisdiccion={jurisdiccion} servicio={servicio} id={id}
        addTurnos={addTurnos}
        onDeleteHistorial={onDeleteHistorial}
        />
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

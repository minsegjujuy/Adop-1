import React from "react";
import { HeaderPage } from "../../components/Admin/";
import { TableVigilancia } from "../../components/Vigilancia/TableVigilancia";
import { CargaVigilancia,AsignarPersonal } from "../Vigilancia";
import { MapView } from "../../components/Vigilancia/Mapa/react-leaflet";
import { CargaHorario } from "../../components/Vigilancia/CargaHorarios";
import { useVigilancia} from "../../hooks";
import { Button, Form } from "semantic-ui-react";
import { useFormik } from "formik";
import { Link, useLocation } from "react-router-dom";
import { ModalBasic } from "../../components/Common/ModalBasic";
import { useEffect, useState } from "react";
import "./HomeAdmin.scss";
// import Swal from "sweetalert2";

export function HomeAdmin() {
  const { get_vigilancia, vigilancias} = useVigilancia();

  const [titleModal, setTitleModal] = useState(null);
  const [showModal, setShowModal] = useState(false);
  const [contentModal, setContentModal] = useState(null);
  const [refetch, setRefetch] = useState(false);
  const { pathname } = useLocation();
  useEffect(() => {
    get_vigilancia();
  }, []);

  const openCloseModal = () => {
    setShowModal((prev) => !prev);
  };
  const onRefetch = () => setRefetch((prev) => !prev);

  const addHorarios = (fecha_fin, fecha_inicio,id) => {
    setTitleModal("Agregar Horarios");
   
    setContentModal(
      <CargaHorario
        onClose={openCloseModal}
        Refetch={onRefetch}
        fecha_fin={fecha_fin}
        fecha_inicio={fecha_inicio}
        id={id}
      />
    );
    openCloseModal();
  };
  const vermapa = (position, comando) => {
    // const {position,setposition} = useState({latitud,longitud})
    console.log(position);
    setTitleModal("Ubicacion de Vigilancia");
    setContentModal(
      <div className="mapa">
        <MapView position={position} comando={comando} />
      </div>
    );
    openCloseModal();
  };

  
  const formik = useFormik({
    // initialValues: initialValues(),
    // validationSchema: Yup.object(newSchame()),
    validateOnChange: false,
    onSubmit: async (formValue) => {
      try {
      } catch (error) {
        console.error(error);
      }
    },
  });
  return (
    <>
      <HeaderPage title="VIGILANCIAS" />
      <div className="header-page-vigilancia">
        <div className="formulario-buscar">
          <Form className="add-edit-user-form" onSubmit={formik.handleSubmit}>
            <div className="contenido-buscar-recargar">
              <div className="contenido-formulario-buscar">
                <div style={{ marginRight: "20px" }}>
                  <Form.Input
                    // name="num_doc"
                    placeholder="Id vigilancia"
                    type="number"
                    // value={formik.values.num_doc}
                    // onChange={formik.handleChange}
                    // error={formik.errors.num_doc}
                  />
                </div>

                <Button positive type="submit">
                  {"BUSCAR"}
                </Button>
              </div>

              <div></div>
            </div>
          </Form>
        </div>
        <div className="agregar">
          <Button
            as={Link}
            to={"/admin/carga/vigilancia"}
            active={pathname === "/admin/carga/vigilancia"}
            positive
            onClick={() => <CargaVigilancia />}
          >
            {"AGREGAR NUEVA VIGILANCIA"}
          </Button>
        </div>
      </div>
      <TableVigilancia
        vigilancias={vigilancias}
        AsignarPersonal={AsignarPersonal}
        addHorarios={addHorarios}
        vermapa={vermapa}
      />
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

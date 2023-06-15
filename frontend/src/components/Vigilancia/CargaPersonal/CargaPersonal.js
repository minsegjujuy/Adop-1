import React, { useState, useEffect } from "react";
import { Button, Form, Icon, Checkbox, Input } from "semantic-ui-react";
import { useVigilancia, useAuth } from "../../../hooks";
import { useFormik } from "formik";
import {TableHistorial} from "../../Vigilancia"
import { map } from "lodash";
import * as Yup from "yup";
// import { useAuth} from "../../hooks";
import { toast, Flip } from "react-toastify";
import Swal from "sweetalert2";
import "./CargaPersonal.scss";
export function CargaPersonal(props) {
  const { jurisdiccion, servicio, id, addTurnos,onDeleteHistorial } =
    props;
  const { get_turno, turno} = useVigilancia();
  const [personal, setPersonal] = useState(null);
  const { auth } = useAuth();
  useEffect(() => {
    get_turno(id);
    if (turno?.duracion) {
      formik.setFieldValue("duracion", turno.duracion);
    }
  }, [turno?.duracion]);
  // Obtener la fecha actual
  var fechaActual = new Date();

  // Obtener el día, mes y año de la fecha actual
  var dia = fechaActual.getDate();
  var mes = fechaActual.getMonth() + 1; // Los meses en JavaScript comienzan desde 0, por lo que se suma 1
  var año = fechaActual.getFullYear();

  // Formatear la fecha en el formato deseado (opcional)
  var fechaFormateada = dia + "/" + mes + "/" + año;

  const formik = useFormik({
    initialValues: initialValues(
      jurisdiccion,
      servicio,
      fechaFormateada,
      turno?.duracion ,
    ),
    validationSchema: Yup.object(validationSchema()),
    onSubmit: async (formValue) => {
      try {
        console.log("hola mundo");
        console.log(turno?.duracion)
      } catch (error) {
        toast.error(error.message);
      }
    },
  });

  return (
    <Form>
      
        <>
          <h4 className="ui dividing header">
            Duracion y fecha de la vigilancia
          </h4>
          <div className="two fields">
            <div className="field">
              <label>Duracion (hs)</label>
              <Form.Input
                name="duracion"
                value={formik.values.duracion}
                readOnly
                error
              />
            </div>
            <div className="field">
              <label>Fecha de hoy</label>
              <Form.Input
                name="fecha"
                value={formik.values.fecha}
                readOnly
                error={formik.errors.fecha}
              />
            </div>
          </div>
        
        <h4 className="ui dividing header">Datos sobre la vigilancia</h4>
        <div className="two fields">
          <div className="field">
            <label>Jurisdiccion</label>
            <Form.Input
              name="jurisdiccion"
              value={formik.values.jurisdiccion}
              readOnly
              error={formik.errors.jurisdiccion}
            />
          </div>
          <div className="field">
            <label>Tipo de Servicio</label>
            <Form.Input
              name="tipo_servicio"
              value={formik.values.tipo_servicio}
              readOnly
              error={formik.errors.tipo_servicio}
            />
          </div>
        </div>
      

      <div className="field">
        <h4 className="ui dividing header">
          Personal
        </h4>
       
          <Button
            className="pencil alternate"
            positive
            onClick={() => addTurnos(turno?.turno,turno?.duracion,id)}
          >
            <Icon size="small" className="pencil alternate" />
            Presione aqui para empezar asignar los turnos
          </Button>
        
      </div>
      <h3 className="ui dividing header">Historial </h3>
      <TableHistorial onDeleteHistorial={onDeleteHistorial}/>
      </>
    </Form>
  );
}

function initialValues(
 
  jurisdiccion,
  servicio,
  fechaFormateada,
  duracion
) {
  return {
    jurisdiccion: jurisdiccion,
    tipo_servicio: servicio,
    fecha: fechaFormateada,
    duracion:duracion? duracion:"",
  };
}

function validationSchema() {
  return {
    // password: Yup.string().required(true),
    // nuevacontraseña: Yup.string().required(true),
  };
}

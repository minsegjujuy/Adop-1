import React, { useState, useEffect } from "react";
import { Button, Form, Icon, Checkbox, Input } from "semantic-ui-react";
import { useFormik } from "formik";
import { map } from "lodash";
import * as Yup from "yup";
// import { useAuth} from "../../hooks";
import { toast, Flip } from "react-toastify";
import Swal from "sweetalert2";
import "./CargaPersonal.scss";
export function CargaPersonal(props) {
  const { fecha_fin, fecha_inicio,jurisdiccion,servicio } = props;
  console.log(fecha_fin, fecha_inicio,jurisdiccion);

  const recursos = [
    { key: "1", text: "EMPLEADO 1", value: 1 },
    { key: "2", text: "EMPLEADO 2", value: 2 },
    { key: "3", text: "EMPLEADO 3", value: 3 },
    { key: "4", text: "EMPLEADO 4", value: 4 },
    { key: "5", text: "EMPLEADO 5", value: 5 },
    { key: "6", text: "EMPLEADO 6", value: 6 },
    { key: "7", text: "EMPLEADO 7", value: 7 },
    { key: "8", text: "EMPLEADO 8", value: 8 },
  ];

  let arreglo2 = [
    {
      legajo: "",
      nombre:"",
      turno: "",
    },
    {
      legajo: "",
      nombre:"",
      turno: "",
    },
    {
      legajo: "",
      nombre:"",
      turno: "",
    },
    {
      legajo: "",
      nombre:"",
      turno: "",
    },
  ];

  let arreglo3 = redimension(arreglo2,3)
  console.log(arreglo3)
  const formik = useFormik({
    initialValues: initialValues(fecha_inicio, fecha_fin, arreglo3,jurisdiccion,servicio),
    validationSchema: Yup.object(validationSchema()),
    onSubmit: async (formValue) => {
      try {
        console.log(formValue);
      } catch (error) {
        toast.error(error.message);
      }
    },
  });

  return (
    <Form>
      <div class="ui form">
      <h4 className="ui dividing header">Datos sobre la vigilancia</h4>
        <div class="two fields">
          <div class="field">
            <label>Jurisdiccion</label>
            <Form.Input
              name="jurisdiccion"
              value={formik.values.jurisdiccion}
              // onChange={formik.handleChange}
              error={formik.errors.jurisdiccion}
            />
          </div>
          <div class="field">
            <label>Tipo de Servicio</label>
            <Form.Input
              name="tipo_servicio"
              value={formik.values.tipo_servicio}
              // onChange={formik.handleChange}
              error={formik.errors.tipo_servicio}
            />
          </div>
        </div>
      </div>
      
      {/* <div class="two fields">
          <div class="field">
            <label>FECHA INICIO DE LA VIGILANCIA</label>
            <Form.Input
              name="fecha_inicio"
              type="date"
              value={formik.values.fecha_inicio}
              // onChange={formik.handleChange}
              error={formik.errors.fecha_inicio}
            />
          </div>
          <div class="field">
            <label>FECHA FIN DE LA VIGILANCIA</label>
            <Form.Input
              name="fecha_fin"
              type="date"
              value={formik.values.fecha_fin}
              // onChange={formik.handleChange}
              error={formik.errors.fecha_fin}
            />
          </div>
        </div> */}
      <h4 className="ui dividing header">Personal Asignado a la vigilancia</h4>
      {map(arreglo3, (arreglo3, index) => (
        
          <div class="three fields">
            <div class="field">
              <label>Legajo</label>
              <div class="field">
                <Form.Select
                  search
                  name={`Turnos[${index}].legajo`}
                  options={recursos}
                  placeholder="Buscar Legajo "
                  value={formik.values.Turnos.legajo}
                  onChange={(_, data) =>
                    formik.setFieldValue(`Turnos[${index}].legajo`, data.value)
                  }
                />
              </div>
            </div>
            <div class="field">
              <label>Nombre y Apellido</label>
              <div class="field">
                <Form.Input
                  name={`Turnos[${index}].nombre`}
                  placeholder="Nombre y Apellido"
                  value={formik.values.Turnos.nombre}
                  onChange={formik.handleChange}
                  error={formik.errors.Turnos?.nombre}
                />
              </div>
            </div>
            <div class="field">
              <label>Horario del turno</label>
              <div class="field">
                <Form.Input
                  name={`Turnos[${index}].hora_inicial`}
                  type="time"
                  placeholder="Indique la hora inicial"
                  value={formik.values.Turnos.hora_inicial}
                  onChange={formik.handleChange}
                  error={formik.errors.Turnos?.hora_inicial}
                />
              </div>
            </div>
          </div>
        
      ))}
    </Form>
  );
}

function initialValues(fecha_inicio, fecha_fin, arreglo3,jurisdiccion,servicio) {
  return {
    jurisdiccion:jurisdiccion,
    tipo_servicio:servicio,
    fecha_inicio: fecha_inicio,
    fecha_fin: fecha_fin,
    Turnos: arreglo3,
  };
}
function redimension(arreglo2, n) {
 
  return arreglo2.slice(0, n);
}

function validationSchema() {
  return {
    // password: Yup.string().required(true),
    // nuevacontraseña: Yup.string().required(true),
  };
}

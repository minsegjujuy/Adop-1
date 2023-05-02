import React, { useState, useEffect } from "react";
import { Button, Form, Icon, Checkbox, Input } from "semantic-ui-react";
import { useFormik } from "formik";
import * as Yup from "yup";
// import { useAuth} from "../../hooks";
import { toast, Flip } from "react-toastify";
import Swal from "sweetalert2";
import "./CargaPersonal.scss";
export function CargaPersonal(props) {
   
  const {fecha_fin,fecha_inicio} = props
  console.log(fecha_fin,fecha_inicio)

  const recursos = [
    { key: "1", text: "EMPLEADO 1", value: 1 },
    { key: "2", text: "EMPLEADO 2", value: 2 },
    { key: "3", text: "EMPLEADO 3", value: 3 },
    { key: "4", text: "EMPLEADO 4", value: 4 },
    { key: "5", text: "EMPLEADO 5", value: 5 },
    { key: "6", text: "EMPLEADO 6", value: 6 },
    { key: "7", text: "EMPLEADO 7", value: 7 },
    { key: "8", text: "EMPLEADO 8", value: 8 }]
  const formik = useFormik({
    initialValues: initialValues(fecha_inicio,fecha_fin),
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
        <div class="two fields">
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
        </div>
        <div class="field">
    <label>LEGAJO</label>
    <Form.Select
              search
              name="legajo"
              options={recursos}
              placeholder="Buscar Legajo "
              value={formik.values.legajo}
              onChange={(_, data) =>
                formik.setFieldValue("legajo", data.value)
              }
            />
  </div>
      </div>
    </Form>
  );
}

function initialValues(fecha_inicio,fecha_fin) {
  return {
    fecha_inicio: fecha_inicio,
    fecha_fin:fecha_fin,
  };
}

function validationSchema() {
  return {
    // password: Yup.string().required(true),
    // nuevacontraseña: Yup.string().required(true),
  };
}

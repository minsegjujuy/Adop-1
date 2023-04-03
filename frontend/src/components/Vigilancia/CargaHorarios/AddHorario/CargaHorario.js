import React, { useState, useEffect } from "react";
import { useFormik } from "formik";
import { Table, Form, Button, Select, Checkbox } from "semantic-ui-react";
import { map } from "lodash";
import Swal from "sweetalert2";
import * as Yup from "yup";

export const CargaHorario = (props) => {
  const { onClose, cantidad_dias, setformHorario } = props;
  //   const { addFranja, obtenerFranjas } = usePacienteDiabetes();

  const arreglo = [
    {
      turno_completo: false,
      hora_inicial: "",
      hora_final: "",
      fecha_vigilancia: "",
      dia_semana: "",
    },
  ];
  const arreglo2 = definirVector(arreglo, cantidad_dias);

  const dias = [
    { key: "1", text: "Lunes", value: "Lunes" },
    { key: "2", text: "Martes", value: "Martes" },
    { key: "3", text: "Miercoles", value: "Miercoles" },
    { key: "4", text: "Jueves", value: "Jueves" },
    { key: "5", text: "Viernes", value: "Viernes" },
  ];

  // useEffect(() => {
  //   definirVector(arreglo,cantidad_dias)
  // }, []);

  const formik = useFormik({
    initialValues: initialValues(arreglo2),
    validationSchema: Yup.object(newSchema()),
    validateOnChange: false,
    onSubmit: async (formValue) => {
      try {
        console.log("hola mundo");
        console.log(cantidad_dias);
        console.log(formValue);
        setformHorario(formValue);
        onClose();
      } catch (error) {}
    },
  });

  return (
    <Form className="add-edit-use-form" onSubmit={formik.handleSubmit}>
      {map(arreglo2, (arreglo2, index) => (
        <div class="five fields">
          <div class="field">
            <label>Dia completo {index}</label>
            <div class="field">
              <Checkbox
                toggle
                checked={formik.values.Turnos.turno_completo}
                onChange={(_, data) => {
                  formik.setFieldValue(
                    `Turnos[${index}].turno_completo`,
                    data.checked
                  );
                }}
              />{" "}
            </div>
          </div>

          {formik.values.Turnos[`${index}`].turno_completo === false && (
            <div class="field">
              <label>Hora inicial</label>
              <Form.Input
                name={`Turnos[${index}].hora_inicial`}
                type="time"
                placeholder="Indique la hora inicial"
                value={formik.values.Turnos.hora_inicial}
                onChange={formik.handleChange}
                error={formik.errors.Turnos?.hora_inicial}
              />
            </div>
          )}

          {formik.values.Turnos[`${index}`].turno_completo === false && (
            <div class="field">
              <label>Hora_final</label>
              <Form.Input
                name={`Turnos[${index}].hora_final`}
                type="time"
                placeholder="Indique la hora final"
                value={formik.values.Turnos.hora_final}
                onChange={formik.handleChange}
                error={formik.errors.Turnos?.hora_final}
              />
            </div>
          )}
          <div class="field">
            <label>Fecha</label>
            <div class="field">
              <Form.Input
                name={`Turnos[${index}].fecha_vigilancia`}
                type="date"
                placeholder="Indique la fecha de la vigilancia"
                value={formik.values.Turnos.fecha_vigilancia}
                onChange={formik.handleChange}
                error={formik.errors.Turnos?.fecha_vigilancia}
              />
            </div>
          </div>
          {formik.values.Turnos[`${index}`].turno_completo === false && (
            <div class="field">
              <label>Dia semana</label>
              <Form.Select
                fluid
                name={`Turnos[${index}].dia_semana`}
                options={dias}
                placeholder="dia"
                value={formik.values.Turnos.dia_semana}
                onChange={(_, data) =>
                  formik.setFieldValue(
                    `Turnos[${index}].dia_semana`,
                    data.value
                  )
                }
              />
            </div>
          )}
        </div>
      ))}

      <Button type="submit" primary fluid content={"Guardar "} />
    </Form>
  );
};

function initialValues(Turnos) {
  return {
    Turnos,
  };
}
function definirVector(arreglo, cantidad_dias) {
  for (let i = 0; i < cantidad_dias; i++) {
    arreglo[i] = {
      turno_completo: false,
      hora_inicial: "",
      hora_final: "",
      fecha_vigilancia: "",
      dia_semana: "",
    };
  }
  return arreglo;
}
function newSchema() {
  return {
    hora_inicial: Yup.string(),
  };
}

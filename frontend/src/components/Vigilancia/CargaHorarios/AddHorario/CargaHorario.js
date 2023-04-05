import React, { useState, useEffect } from "react";
import { useFormik } from "formik";
import { Table, Form, Button, Select, Checkbox ,TimeInput} from "semantic-ui-react";
import { map } from "lodash";
import Swal from "sweetalert2";
import * as Yup from "yup";
import "./CargaHorario.scss"

export const CargaHorario = (props) => {
  const { onClose, cantidad_dias, setformHorario } = props;
  //   const { addFranja, obtenerFranjas } = usePacienteDiabetes();

  // const arreglo = [
  //   {
  //     turno_completo: false,
  //     hora_inicial: "",
  //     hora_final: "",
  //     fecha_vigilancia: "",
  //     dia_semana: "",
  //   },
  // ];
  // const arreglo2 = definirVector(arreglo, cantidad_dias);
  const today = new Date();
  const dia_semana = today.getDay();

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
    initialValues: initialValues(),
    validationSchema: Yup.object(newSchema()),
    validateOnChange: false,
    onSubmit: async (formValue) => {
      try {
        // console.log("hola mundo");
        // console.log(cantidad_dias);
        // console.log(formValue);
        // setformHorario(formValue);
        console.log(dia_semana)
        onClose();
      } catch (error) {}
    },
  });

  return (
    <Form className="add-edit-use-form" onSubmit={formik.handleSubmit}>
      <div>
        <div class="seven fields">
        {dia_semana <= 1 &&(
          <div class="field">
            
            <label>Lunes </label>
            <div class="field">
              <Checkbox
                checked={formik.values.lunes}
                onChange={(event, data) =>
                  formik.setFieldValue("lunes", data.checked)
                }
              />
            </div>
          </div>
     )}
     {dia_semana <= 2 &&(
          <div class="field">
            <label>Martes</label>
            <Checkbox
            
              checked={formik.values.martes}
              onChange={(event, data) =>
                formik.setFieldValue("martes", data.checked)
              }
            />
          </div>
     )}
     {dia_semana <= 3 &&(
          <div class="field">
            <label>Miercoles</label>
            <Checkbox
              
              checked={formik.values.miercoles}
              onChange={(event, data) =>
                formik.setFieldValue("miercoles", data.checked)
              }
            />
          </div>
     )}
       {dia_semana <= 4 &&(
          <div class="field">
            <label>Jueves</label>
            <div class="field">
              <Checkbox
               
                checked={formik.values.jueves}
                onChange={(event, data) =>
                  formik.setFieldValue("jueves", data.checked)
                }
              />
            </div>
          </div>
       )}
       {dia_semana <= 5 &&(
          <div class="field">
            <label>Viernes</label>
            <Checkbox
             
              checked={formik.values.viernes}
              onChange={(event, data) =>
                formik.setFieldValue("viernes", data.checked)
              }
            />
          </div>
       )}
       {dia_semana <= 6 &&(

          <div class="field">
            <label>Sabado</label>
            <Checkbox
             
              checked={formik.values.sabado}
              onChange={(event, data) =>
                formik.setFieldValue("sabado", data.checked)
              }
            />
          </div>
       )}
       {dia_semana <= 6 &&(
          <div class="field">
            <label>Domingo</label>
            <Checkbox
              
              checked={formik.values.domingo}
              onChange={(event, data) =>
                formik.setFieldValue("domingo", data.checked)
              }
            />
          </div>
       )}
        </div>
       

        <div class="three fields">
          <div class="field">
            <label>Dia completo </label>

            <div class="field">
              <Checkbox
                toggle
                checked={formik.values.turno_completo}
                onChange={(_, data) => {
                  formik.setFieldValue("turno_completo", data.checked);
                }}
              />{" "}
            </div>
          </div>
          {formik.values.turno_completo === false && (
            <div class="field">
              <label>Hora de inicio</label>
              <Form.Input
                name="hora_inicio"
                type="time"
                placeholder="Ingrese hora inicio"
                value={formik.values.hora_inicio}
                onChange={formik.handleChange}
                error={formik.errors.hora_inicio}
              />
            </div>
          )}
          {formik.values.turno_completo === false && (
            <div class="field">
              <label>Hora final</label>
              <div class="field">
                <Form.Input
                  name="hora_fin"
                  type="time"
                  placeholder="Ingrese hora final"
                  value={formik.values.hora_fin}
                  onChange={formik.handleChange}
                  error={formik.errors.hora_fin}
                />
              </div>
            </div>
          )}
        </div>
      </div>

      {/* <div className="dias_semana">
      <Checkbox
        label="Lunes"
        checked={formik.values.lunes}
        onChange={(event, data) => formik.setFieldValue("lunes", data.checked)}
      />
      <Checkbox
        label="Martes"
        checked={formik.values.martes}
        onChange={(event, data) => formik.setFieldValue("martes", data.checked)}
      />
      <Checkbox
        label="Miércoles"
        checked={formik.values.miercoles}
        onChange={(event, data) =>
          formik.setFieldValue("miercoles", data.checked)
        }
      />
      <Checkbox
        label="Jueves"
        checked={formik.values.jueves}
        onChange={(event, data) => formik.setFieldValue("jueves", data.checked)}
      />
      <Checkbox
        label="Viernes"
        checked={formik.values.viernes}
        onChange={(event, data) =>
          formik.setFieldValue("viernes", data.checked)
        }
      />
      <Checkbox
        label="Sábado"
        checked={formik.values.sabado}
        onChange={(event, data) => formik.setFieldValue("sabado", data.checked)}
      />
      <Checkbox
        label="Domingo"
        checked={formik.values.domingo}
        onChange={(event, data) =>
          formik.setFieldValue("domingo", data.checked)
        }
      />
     </div> */}
      <Button type="submit" primary fluid content={"Asignar "} />
    </Form>
  );
};

function initialValues(Turnos) {
  return {
    lunes:false,
    martes:false,
    miercoles:false,
    jueves:false,
    viernes:false,
    sabado:false,
    domingo:false,
    turno_completo:false,
    hora_inicio:"",
    hora_fin:"",
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

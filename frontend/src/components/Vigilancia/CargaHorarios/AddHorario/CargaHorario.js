import React, { useState, useEffect } from "react";
import { useFormik } from "formik";
import {
  Table,
  Form,
  Button,
  Select,
  Checkbox,
  TimeInput,
} from "semantic-ui-react";
import { map } from "lodash";
import Swal from "sweetalert2";
import * as Yup from "yup";
import "./CargaHorario.scss";

export const CargaHorario = (props) => {
  const { onClose, fecha_fin,fecha_inicio } = props;
  
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

  // const today = new Date();
  // const dia_semana = today.getDay();
  // let dia = ("0" + today.getDate()).slice(-2);
  // let mes = ("0" + (today.getMonth() + 1)).slice(-2);
  // let anio = today.getFullYear().toString();
  // let fechaformateada = anio + "-" + mes + "-" + dia;

  const fecha1 = new Date(fecha_inicio);
  const fecha2 = new Date(fecha_fin? fecha_fin:"2026-01-01");
  const unDia = 24 * 60 * 60 * 1000; // número de milisegundos en un día
  const diffFechas = Math.abs(fecha2 - fecha1); // diferencia de milisegundos entre las fechas
  const diferencia = Math.floor(diffFechas / unDia); // redondea hacia abajo al número entero más cercano

  const cant_semanas = Math.floor(diferencia / 7);
  const dias_ult_semana = diferencia % 7;

  const dias = [
    { key: "1", text: "Lunes", value: "Lunes" },
    { key: "2", text: "Martes", value: "Martes" },
    { key: "3", text: "Miercoles", value: "Miercoles" },
    { key: "4", text: "Jueves", value: "Jueves" },
    { key: "5", text: "Viernes", value: "Viernes" },
  ];

  
  let turnos = [];
  let dias_semana=[]
 

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
        // console.log(dia_semana)

          let turnos2 = [];
          if (formValue.lunes === true) {
            turnos2.push("lunes")
          }
          if (formValue.martes === true) {
            turnos2.push("martes")
          }
          if (formValue.miercoles === true) {
            turnos2.push("miercoles")
          }
          if (formValue.jueves === true) {
            turnos2.push("jueves")
          }
          if (formValue.viernes === true) {
            turnos2.push("viernes")
          }
          if (formValue.sabado === true) {
            turnos2.push("sabado")
          }
          if (formValue.domingo === true) {
            turnos2.push("domingo")
          }
          console.log(...turnos2)
          turnos.push(turnos2)
          console.log(turnos)
          let ultima_semana=[]
          if(dias_ult_semana!==0){
            
            if (formValue.lunes === true && (dias_ult_semana>=1)) {
              ultima_semana.push("lunes")
            }
            if (formValue.martes === true && (dias_ult_semana>=2)) {
              ultima_semana.push("martes")
            }
            if (formValue.miercoles === true && (dias_ult_semana>=3)) {
              ultima_semana.push("miercoles")
            }
            if (formValue.jueves === true && (dias_ult_semana>=4)) {
              ultima_semana.push("jueves")
            }
            if (formValue.viernes === true && (dias_ult_semana>=5)) {
              ultima_semana.push("viernes")
            }
            if (formValue.sabado === true && (dias_ult_semana>=6)) {
              ultima_semana.push("sabado")
            }
            if (formValue.domingo === true && (dias_ult_semana>=7)) {
              ultima_semana.push("domingo")
            }
          }
        

        const formValue2 = {
          
          turno:[fecha_fin? cant_semanas:1,{turnos},fecha_fin? ultima_semana:[]],
          turno_completo: formValue.turno_completo,
          hora_inicio: formValue.hora_inicio,
          hora_fin: formValue.hora_fin,
        };
        console.log(fecha_inicio);
        console.log(fecha_fin)
        console.log(diferencia);
        console.log(cant_semanas);
        console.log(dias_ult_semana);
        console.log(formValue2);
        // onClose();
      } catch (error) {}
    },
  });

  return (
    <Form className="add-edit-use-form" onSubmit={formik.handleSubmit}>
      <div>
        <div class="seven fields">
          
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
          
         
            <div class="field">
              <label>Martes</label>
              <Checkbox
                checked={formik.values.martes}
                onChange={(event, data) =>
                  formik.setFieldValue("martes", data.checked)
                }
              />
            </div>
          
          
            <div class="field">
              <label>Miercoles</label>
              <Checkbox
                checked={formik.values.miercoles}
                onChange={(event, data) =>
                  formik.setFieldValue("miercoles", data.checked)
                }
              />
            </div>
          
         
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
          
          
            <div class="field">
              <label>Viernes</label>
              <Checkbox
                checked={formik.values.viernes}
                onChange={(event, data) =>
                  formik.setFieldValue("viernes", data.checked)
                }
              />
            </div>
          
          
            <div class="field">
              <label>Sabado</label>
              <Checkbox
                checked={formik.values.sabado}
                onChange={(event, data) =>
                  formik.setFieldValue("sabado", data.checked)
                }
              />
            </div>
          
         
            <div class="field">
              <label>Domingo</label>
              <Checkbox
                checked={formik.values.domingo}
                onChange={(event, data) =>
                  formik.setFieldValue("domingo", data.checked)
                }
              />
            </div>
          
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
    lunes: false,
    martes: false,
    miercoles: false,
    jueves: false,
    viernes: false,
    sabado: false,
    domingo: false,
    turno_completo: false,
    hora_inicio: "",
    hora_fin: "",
  };
}
function definirVector(turno, cant_semanas, cant_dias) {
  if (cant_dias !== 0) {
    cant_semanas = cant_semanas + 1;
  }
  for (let index = 0; index < cant_semanas; index++) {
    turno[index] = {
      lunes: false,
      martes: false,
      miercoles: false,
      jueves: false,
      viernes: false,
      sabado: false,
      domingo: false,
    };
  }
  return turno;
}
function newSchema() {
  return {
    hora_inicial: Yup.string(),
  };
}

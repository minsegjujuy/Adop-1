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
  const { onClose, fecha_fin, fecha_inicio, id } = props;

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
  // const dianuevo = formatearfecha(dia_semana);
  // let dia = ("0" + today.getDate()).slice(-2);
  // let mes = ("0" + (today.getMonth() + 1)).slice(-2);
  // let anio = today.getFullYear().toString();
  // let fechaformateada = anio + "-" + mes + "-" + dia;

  // const fecha1 = new Date(fechaformateada);
  // const fecha2 = new Date(fecha_fin? fecha_fin:"2026-01-01");
  // const unDia = 24 * 60 * 60 * 1000; // número de milisegundos en un día
  // const diffFechas = Math.abs(fecha2 - fecha1); // diferencia de milisegundos entre las fechas
  // const diferencia = Math.floor(diffFechas / unDia); // redondea hacia abajo al número entero más cercano

  // const cant_semanas = Math.floor(diferencia / 7);
  // const dias_ult_semana = diferencia % 7;

  // const dias = [
  //   { key: "1", text: "Lunes", value: "Lunes" },
  //   { key: "2", text: "Martes", value: "Martes" },
  //   { key: "3", text: "Miercoles", value: "Miercoles" },
  //   { key: "4", text: "Jueves", value: "Jueves" },
  //   { key: "5", text: "Viernes", value: "Viernes" },
  // ];

  let turnos = [];
  // let turnos_media=[];

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
       
        if (formValue.lunes === true) {
          turnos.push("lunes");
        }
        if (formValue.martes === true) {
          turnos.push("martes");
        }
        if (formValue.miercoles === true) {
          turnos.push("miercoles");
        }
        if (formValue.jueves === true) {
          turnos.push("jueves");
        }
        if (formValue.viernes === true) {
          turnos.push("viernes");
        }
        if (formValue.sabado === true) {
          turnos.push("sabado");
        }
        if (formValue.domingo === true) {
          turnos.push("domingo");
        }
        //   console.log(...turnos2)
        //   turnos.push(turnos2)
        //   console.log(turnos)
        //   let turnos3=[];
        //   if(cant_semanas>1){
        //     if (formValue.lunes === true)  {
        //       turnos3.push("lunes")
        //     }
        //     if (formValue.martes === true)  {
        //       turnos3.push("martes")
        //     }
        //     if (formValue.miercoles === true)  {
        //       turnos3.push("miercoles")
        //     }
        //     if (formValue.jueves === true) {
        //       turnos3.push("jueves")
        //     }
        //     if (formValue.viernes === true)  {
        //       turnos3.push("viernes")
        //     }
        //     if (formValue.sabado === true) {
        //       turnos3.push("sabado")
        //     }
        //     if (formValue.domingo === true)  {
        //       turnos3.push("domingo")
        //     }
        //     turnos_media.push(turnos3)
        //   }
        //   let ultima_semana=[]
        //   if(dias_ult_semana!==0){

        //     if (formValue.lunes === true && (dias_ult_semana>=1)) {
        //       ultima_semana.push("lunes")
        //     }
        //     if (formValue.martes === true && (dias_ult_semana>=2)) {
        //       ultima_semana.push("martes")
        //     }
        //     if (formValue.miercoles === true && (dias_ult_semana>=3)) {
        //       ultima_semana.push("miercoles")
        //     }
        //     if (formValue.jueves === true && (dias_ult_semana>=4)) {
        //       ultima_semana.push("jueves")
        //     }
        //     if (formValue.viernes === true && (dias_ult_semana>=5)) {
        //       ultima_semana.push("viernes")
        //     }
        //     if (formValue.sabado === true && (dias_ult_semana>=6)) {
        //       ultima_semana.push("sabado")
        //     }
        //     if (formValue.domingo === true && (dias_ult_semana>=7)) {
        //       ultima_semana.push("domingo")
        //     }
        //   }

        const formValue2 = {
          turno: formValue.diario===true? null:turnos,
          dia_completo: formValue.turno_completo,
          fecha_fin: fecha_fin,
          fecha_inicio: fecha_inicio,
          fk_vigilancia: id,
          diario:formValue.diario,
          hora_inicio:formValue.turno_completo? null:formValue.hora_inicio,
          hora_fin:formValue.turno_completo? null:formValue.hora_fin,
        };
        // console.log(fecha_inicio);
        // console.log(fecha_fin)
        // console.log(diferencia);
        // console.log(cant_semanas);
        // console.log(dias_ult_semana);
        console.log(formValue2);
        //   if(response.msj){
        //     Swal.fire({
        //       title: "Exito!",
        //       text: response.msj,
        //       icon: "success",
        //       timer: 3000,
        //       showConfirmButton: true,
        //     });
        //     window.location.replace("http://localhost:3000/admin/vigilancia");
        //   }else{
        //     Swal.fire({
        //       title: "Algunos datos ingresados no son validos!",
        //       text: response.msj,
        //       icon: "error",
        //       showConfirmButton: true,
        //     });

        // }
        // onClose();
      } catch (error) {}
    },
  });

  return (
    <Form className="add-edit-use-form" onSubmit={formik.handleSubmit}>
      <div>
        {!formik.values.diario &&(
        <div className="seven fields">
          <div className="field">
            <label>Lunes </label>
            <div className="field">
              <Checkbox
                checked={formik.values.lunes}
                onChange={(event, data) =>
                  formik.setFieldValue("lunes", data.checked)
                }
              />
            </div>
          </div>

          <div className="field">
            <label>Martes</label>
            <Checkbox
              checked={formik.values.martes}
              onChange={(event, data) =>
                formik.setFieldValue("martes", data.checked)
              }
            />
          </div>

          <div className="field">
            <label>Miercoles</label>
            <Checkbox
              checked={formik.values.miercoles}
              onChange={(event, data) =>
                formik.setFieldValue("miercoles", data.checked)
              }
            />
          </div>

          <div className="field">
            <label>Jueves</label>
            <div className="field">
              <Checkbox
                checked={formik.values.jueves}
                onChange={(event, data) =>
                  formik.setFieldValue("jueves", data.checked)
                }
              />
            </div>
          </div>

          <div className="field">
            <label>Viernes</label>
            <Checkbox
              checked={formik.values.viernes}
              onChange={(event, data) =>
                formik.setFieldValue("viernes", data.checked)
              }
            />
          </div>

          <div className="field">
            <label>Sabado</label>
            <Checkbox
              checked={formik.values.sabado}
              onChange={(event, data) =>
                formik.setFieldValue("sabado", data.checked)
              }
            />
          </div>

          <div className="field">
            <label>Domingo</label>
            <Checkbox
              checked={formik.values.domingo}
              onChange={(event, data) =>
                formik.setFieldValue("domingo", data.checked)
              }
            />
          </div>
        </div>
        )}
        <div className="field">
            <label>Vigilancia Diaria</label>
            <Checkbox
                  toggle
                  checked={formik.values.diario}
                  onChange={(_, data) => {
                    formik.setFieldValue("diario", data.checked);
                  }}
                />
          </div>

        <div className="three fields">
          <div className="field">
            <label>Dia completo </label>

            <div className="field">
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
            <div className="field">
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
            <div className="field">
              <label>Hora final</label>
              <div className="field">
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
    diario:false,
    hora_inicio: "",
    hora_fin: "",
  };
}
// function formatearfecha(dia_semana) {
//   if (dia_semana===0) {
//     dia_semana=7;
//   }
//   return dia_semana;
// }
function newSchema() {
  return {
    hora_inicial: Yup.string(),
  };
}

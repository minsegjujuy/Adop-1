import React, { useState, useEffect } from "react";
import { useFormik } from "formik";
import { Form, Button, Select,Checkbox } from "semantic-ui-react";
import { map } from "lodash";
import Swal from "sweetalert2";
import * as Yup from "yup";

export const CargaHorario = (props) => {
     const { cantidad_dias } = props;
//   const { addFranja, obtenerFranjas } = usePacienteDiabetes();
     
     const arreglo=[{
      turno_completo:false,
      // hora_inicial: "",
      // hora_final:"",
      // fecha_vigilancia:"",
     }];
     const arreglo2= definirVector(arreglo,cantidad_dias);



// useEffect(() => {
//   definirVector(arreglo,cantidad_dias)
// }, []);

  const formik = useFormik({
    initialValues: initialValues(arreglo2),
    validationSchema: Yup.object(newSchema()),
    validateOnChange: false,
    onSubmit: async (formValue) => {
      try {
      console.log("hola mundo")
      console.log(cantidad_dias)
      console.log(formValue)
      } catch (error) {
       
      }
    },
  });

  return (
    <Form className="add-edit-use-form" onSubmit={formik.handleSubmit}>

        {map(arreglo2,(arreglo2,index) => (
          <li key={index}>
             {/* <Checkbox
                      toggle
                      checked={formik.values.arreglo2.turno_completo}
                      onChange={(_, data) => {
                        formik.setFieldValue("arreglo2.turno_completo", data.checked);
                      }}
                    />{" "} */}
              <Form.Input
                   name="arreglo2.hora_inicial"
                   placeholder={arreglo2.turno_completo}
                  //  value={formik.values.arreglo2.hora_inicial}
                   onChange={formik.handleChange}
                  // error={formik.errors.arreglo2.hora_inicial}
                  />
            
               {/* <div class="two fields">
               <div class="two fields">
                <div class="field">
                  <label>Dia completo {index}</label>
                  <div class="field">
                    
                    <Checkbox
                      toggle
                      checked={formik.values.arreglo2.turno_completo}
                      onChange={(_, data) => {
                        formik.setFieldValue("arreglo2.turno_completo", data.checked);
                      }}
                    />{" "}
                    </div>
                </div>
                {formik.values.arreglo2.turno_completo===false &&
                <div class="field">
                  <label>Hora inicial</label>
                  <div class="field">
                  <Form.Input
                   name="arreglo2.Hora_inicial"
                   type="time"
                   placeholder="Indique la hora inicial"
                   value={formik.values.arreglo2.hora_inicial}
                   onChange={formik.handleChange}
                  error={formik.errors.arreglo2.hora_inicial}
                  />
                   </div>
                </div>
                }
                </div>
                <div class="two fields">
                {formik.values.arreglo2.turno_completo===false &&
                <div class="field">
                  <label>Hora_final</label>
                  <Form.Input
                   name="arreglo2[{index}].Hora_final"
                   type="time"
                   placeholder="Indique la hora final"
                   value={formik.values.arreglo2.hora_final}
                   onChange={formik.handleChange}
                    error={formik.errors.arreglo2.hora_final}
                  />
                    
                </div>
                }  
                <div class="field">
                  <label>Fecha</label>
                  <div class="field">
                    <Form.Input
                   name="arreglo2.fecha_vigilancia"
                   type="date"
                   placeholder="Indique la fecha de la vigilancia"
                   value={formik.values.arreglo2.fecha_vigilancia}
                   onChange={formik.handleChange}
                    error={formik.errors.fecha_vigilancia}
                   />
                   </div>
                </div>
                </div>
              </div>
               */}

            </li>
        ))}
    

      <Button type="submit" primary fluid content={"Agregar Franja"} />
    </Form>
  );
};

function initialValues(arreglo2) {
 
  return {
      arreglo2
  };}
function definirVector(arreglo,cantidad_dias){
    for (let i = 0; i< cantidad_dias; i++) {  
             arreglo[i]={
              turno_completo:false,
              // hora_inicial: "",
              // hora_final:"",
              // fecha_vigilancia:"",
             }
  }
  return arreglo;
  
}
function newSchema() {
  return {
    hora_inicial: Yup.string(),
  };
}

import React, { useState, useEffect } from "react";
import { Button, Form, Icon, Checkbox, Input } from "semantic-ui-react";
import { useVigilancia, useAuth } from "../../../hooks";
import { useFormik } from "formik";
import { map } from "lodash";
import * as Yup from "yup";
// import { useAuth} from "../../hooks";
import { toast, Flip } from "react-toastify";
import Swal from "sweetalert2";
import "./Personal.scss";
export function Personal(props) {
  const {turnos,duracion} =props;
  const { get_turno, turno, get_personal, asignar_personal } = useVigilancia();
  const [personal, setPersonal] = useState(null);
  const { auth } = useAuth();
  const [horas, sethoras] = useState(false);
  useEffect(() => {
    buscarPersonal();
  }, []);
  const buscarPersonal = async () => {
    const options = await get_personal();

    setPersonal(options.map((option) => option));
  };
  const Cargando = [
    { key: "1", text: "Cargando....", value: 1 },
  ];
  const valores = personal?.map((tipo, index) => ({
    value: tipo.legajo,
    key: `${index}`,
    text: tipo.legajo,
  }));
  const valores2 = personal?.map((tipo, index) => ({
    value: tipo.nombre_apellido,
    key: `${index}`,
    text: tipo.nombre_apellido,
  }));
  const Horario = [
    { key: "1", text: "4 hs", value: 4 },
    { key: "2", text: "5 hs", value: 5 },
  ];
  const fechas = [];
  for (let i = 6; i <= duracion; i++) {
    Horario.push({ key: `${i}`, text: `${i} hs`, value: i });
  }
  for (let i = 0; i <= turnos.length; i++) {
    fechas.push({ key: `${i}`, text: turnos[i], value: turnos[i] });
  }
  const horariosOptions =
    Horario[Horario.length - 1].value === 4
      ? [Horario[Horario.length - 1]]
      : Horario;
  let arreglo3 = [
    {
      legajo: "",
      nombre: "",
      hora_inicio: "",
      turno: "",
    },
    {
      legajo: "",
      nombre: "",
      hora_inicio: "",
      turno: "",
    },
    {
      legajo: "",
      nombre: "",
      hora_inicio: "",
      turno: "",
    },
    {
      legajo: "",
      nombre: "",
      hora_inicio: "",
      turno: "",
    },
    {
      legajo: "",
      nombre: "",
      hora_inicio: "",
      turno: "",
    },
    {
      legajo: "",
      nombre: "",
      hora_inicio: "",
      turno: "",
    },
  ];

  // let arreglo3 = redimension(
  //   arreglo2,
  //   turno?.duracion === 8 ? 1 : turno?.duracion < 24 ? 2 : 3
  // );
  const [numCampos, setNumCampos] = useState(1);

  const campos = [];

  const formik = useFormik({
    initialValues: initialValues(arreglo3, numCampos),
    validationSchema: Yup.object(validationSchema()),
    onSubmit: async (formValue) => {
        let sum = 0;
        let turnos2 = [];
      try {
       
        //     console.log(formValue);
            for (let index = 0; index < formValue.numCampos; index++) {
              // turnos2 = {
              //   fk_personal: formValue.turnos[index].legajo,
              // };
              if (formValue.turnos[index].turno !== "") {
                sum = sum + formValue.turnos[index].turno;
              }
            }
        if (sum === duracion) {
          // const formValue2 = {
          //   fecha: formValue.fecha,
          //   duracion: turno?.duracion,
          //   Turnos: formValue.turnos,
          // };
          // console.log(formValue2);
          console.log(formValue)
          console.log("exito")
          // if (response.msj) {
            Swal.fire({
              title: "Exito!",
              text: "Personal Asignado Correctamente",
              icon: "success",
              timer: 3000,
              showConfirmButton: true,
            });
            // window.location.replace("http://localhost:3000/admin/carga/vigilancia/personal");
          // } else {
          //   Swal.fire({
          //     title: "Algunos datos ingresados no son validos!",
          //     text: response.msj,
          //     icon: "error",
          //     showConfirmButton: true,
          //   });
          // }
        } else {
          Swal.fire({
            title: "Algunos datos ingresados son incorrectos!",
            text:"La cantidad de horas asignadas no es correcta",
            icon: "error",
            showConfirmButton: true,
          });
        }
      } catch (error) {
        toast.error(error.message);
      }
    },
  });
  const handleInputChange = (event) => {
    formik.setFieldValue("numCampos", Number(event.target.value));
    setNumCampos(
      Number(event.target.value) > 6 ? 6 : Number(event.target.value)
    );
    // console.log(cant_turnos)
  };
  for (let i = 0; i < numCampos; i++) {
    campos.push(
      <>
        <div>
          <h4 className="ui dividing header">Personal {i + 1}</h4>
        </div>
        <div className="four fields">
          <div className="field">
            <label>Legajo</label>
            <div className="field">
              <Form.Select
                fluid
                search
                name={`turnos[${i}].legajo`}
                options={valores? valores:Cargando}
                placeholder="Buscar Legajo"
                value={formik.values.turnos[i].legajo}
                onChange={(_, data) =>
                  formik.setFieldValue(`turnos[${i}].legajo`, data.value)
                }
              />
            </div>
          </div>

          <div className="field">
            <label>Nombre y Apellido</label>
            <div className="field">
              <Form.Select
                fluid
                search
                name={`turnos[${i}].nombre`}
                placeholder="Nombre y Apellido"
                options={valores2? valores2:Cargando}
                value={formik.values.turnos[i].nombre}
                onChange={(_, data) =>
                  formik.setFieldValue(`turnos[${i}].nombre`, data.value)
                }
              />
            </div>
          </div>
          <div className="field">
            <label>Horar de inicio</label>
            <div className="field">
              <Form.Input
                fluid
                type="time"
                name={`turnos[${i}].hora_inicio`}
                value={formik.values.turnos[i].hora_inicio}
                onChange={formik.handleChange}
                error={formik.errors.turnos?.hora_inicio}
              />
            </div>
          </div>

          <div className="field">
            <label>Horario del turno</label>
            <div className="field">
              <Form.Select
                fluid
                search
                name={`turnos[${i}].turno`}
                options={horariosOptions}
                placeholder="Asignar Turno"
                value={formik.values.turnos[i].turno}
                onChange={(_, data) =>
                  formik.setFieldValue(`turnos[${i}].turno`, data.value)
                }
              />
            </div>
          </div>
        </div>
      </>
    );
  }
  return (
    <Form onSubmit={formik.handleSubmit}>
      {/* <h4 className="ui dividing header">Personal Asignado a la vigilancia</h4> */}
      <h4 className="ui dividing header">Ingrese la fecha para la vigilancia</h4>
      <div className="one field">
        <Form.Select
          name="fecha_vigilancia"
          options={fechas? fechas:Cargando}
          placeholder="Seleccione la fecha para la vigilancia "
          value={formik.values.fecha_vigilancia}
          onChange={(_, data) =>
            formik.setFieldValue("fecha_vigilancia", data.value)
          }
        />
      </div>

      <h4 className="ui dividing header">Ingrese la cantidad de Turnos de la vigilancia:</h4>
      <div className="one field">
        <input
          type="number"
          min={1}
          max={6}
          placeholder="Ingrese la cantidad de personal para la vigilancia (MAXIMO 6)"
          value={numCampos}
          onChange={handleInputChange}
        />
      </div>
      {/* <h4 className="ui dividing header">Personal</h4> */}
      <div>{campos}</div>
      <div className="boton_crear_vigilancia">
        <Button
          className="positive button"
          type="submit"
          content={"Asignar Personal"}
        />
      </div>
    </Form>
  );
}

function initialValues(arreglo3, numCampos) {
  return {
    fecha_vigilancia:"",
    turnos: arreglo3,
    numCampos,
  };
}

function validationSchema() {
  return {
    // password: Yup.string().required(true),
    // nuevacontraseña: Yup.string().required(true),
  };
}

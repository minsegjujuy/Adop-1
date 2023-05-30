import React, { useState, useEffect } from "react";
import { Button, Form, Icon, Checkbox, Input } from "semantic-ui-react";
import { useVigilancia,useAuth } from "../../../hooks";
import { useFormik } from "formik";
import { map } from "lodash";
import * as Yup from "yup";
// import { useAuth} from "../../hooks";
import { toast, Flip } from "react-toastify";
import Swal from "sweetalert2";
import "./CargaPersonal.scss";
export function CargaPersonal(props) {
  const { fecha_fin, fecha_inicio, jurisdiccion, servicio, id } = props;
  const { get_turno, turno,get_personal } = useVigilancia();
  const [personal,setPersonal]= useState(null)
  const {auth} = useAuth();
  const [horas, sethoras] = useState(false);
  useEffect(() => {
    get_turno(id);
    buscarPersonal();
  }, []);
  const buscarPersonal = async () => {
    const options = await get_personal();
    
    setPersonal(options.map((option) => option));
  };
  const valores = personal?.map((tipo, index) => ({
    value:tipo.legajo,
    key: `${index}`,
    text: tipo.legajo,
  }));
  // Obtener la fecha actual
  var fechaActual = new Date();

  // Obtener el día, mes y año de la fecha actual
  var dia = fechaActual.getDate();
  var mes = fechaActual.getMonth() + 1; // Los meses en JavaScript comienzan desde 0, por lo que se suma 1
  var año = fechaActual.getFullYear();

  // Formatear la fecha en el formato deseado (opcional)
  var fechaFormateada = dia + "/" + mes + "/" + año;

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
  const turnos_vigilancia = [
    { key: "1", text: 1, value: 1 },
    { key: "2", text: 2, value: 2 },
    { key: "3", text: 3, value: 3 },
    { key: "4", text: 4, value: 4 },
    { key: "5", text: 5, value: 5 },
    { key: "6", text: 6, value: 6 },
  ];
  const Horario = [
    { key: "1", text: "4 hs", value: 4 },
    { key: "2", text: "5 hs", value: 5 },
  ];

  for (let i = 6; i <= turno?.duracion; i++) {
    Horario.push({ key: `${i}`, text: `${i} hs`, value: i });
  }
  const horariosOptions =
    Horario[Horario.length - 1].value === 4
      ? [Horario[Horario.length - 1]]
      : Horario;
  let arreglo3 = [
    {
      legajo: "",
      nombre: "",
      hora_inicio:"",
      turno: "",
    },
    {
      legajo: "",
      nombre: "",
      hora_inicio:"",
      turno: "",
    },
    {
      legajo: "",
      nombre: "",
      hora_inicio:"",
      turno: "",
    },
    {
      legajo: "",
      nombre: "",
      hora_inicio:"",
      turno: "",
    },
    {
      legajo: "",
      nombre: "",
      hora_inicio:"",
      turno: "",
    },
    {
      legajo: "",
      nombre: "",
      hora_inicio:"",
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
    initialValues: initialValues(
      fecha_inicio,
      fecha_fin,
      arreglo3,
      jurisdiccion,
      servicio,
      fechaFormateada,
      numCampos
    ),
    validationSchema: Yup.object(validationSchema()),
    onSubmit: async (formValue) => {
      let sum=0
      try {
        console.log(formValue);
        for (let index = 0; index < formValue.numCampos; index++) {
          if(formValue.Turnos[index].turno !== ""){
            sum=sum+formValue.Turnos[index].turno
          }
        }
        if(sum===turno?.duracion){
          console.log(formValue)
          const formValue2={
            fecha:formValue.fecha,
            duracion:turno?.duracion,
            Turnos:formValue.Turnos
          }
          console.log(formValue2)
        }else{
          Swal.fire({
            title: "Algunos datos ingresados son incorrectos!",
            // text: response.msj,
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
    setNumCampos(Number(event.target.value)>6? 6:Number(event.target.value));
    // console.log(cant_turnos)
  };
  for (let i = 0; i < numCampos; i++) {
    
    campos.push(
      
      <div className="four  fields">
        <div class="field">
          <label>Legajo</label>
          <div class="field">
            <Form.Select
              search
              name={`Turnos[${i}].legajo`}
              options={valores}
              placeholder="Buscar Legajo"
              value={formik.values.Turnos[i].legajo}
              onChange={(_, data) =>
                formik.setFieldValue(`Turnos[${i}].legajo`, data.value)
              }
            />
          </div>
        </div>

        <div class="field">
          <label>Nombre y Apellido</label>
          <div class="field">
            <Form.Input
              name={`Turnos[${i}].nombre`}
              placeholder="Nombre y Apellido"
              value={formik.values.Turnos[i].nombre}
              onChange={formik.handleChange}
              error={formik.errors.Turnos?.nombre}
            />
          </div>
        </div>
        <div class="field">
          <label>Horar de inicio</label>
          <div class="field">
            <Form.Input
              type="time"
              name={`Turnos[${i}].hora_inicio`}
              value={formik.values.Turnos[i].hora_inicio}
              onChange={formik.handleChange}
              error={formik.errors.Turnos?.hora_inicio}
            />
          </div>
        </div>

        <div class="field">
          <label>Horario del turno</label>
          <div class="field">
            <Form.Select
              search
              name={`Turnos[${i}].turno`}
              options={horariosOptions}
              placeholder="Asignar Turno"
              value={formik.values.Turnos[i].turno}
              onChange={(_, data) =>
                formik.setFieldValue(`Turnos[${i}].turno`, data.value)
              }
            />
          </div>
        </div>
      </div>
    );
  }
  return (
    <Form onSubmit={formik.handleSubmit}>
      <div class="ui form">
        <div class="field">
          <h4 className="ui dividing header">
            Duracion y fecha de la vigilancia
          </h4>
          <div class="two fields">
            <div class="field">
              <label>Duracion (hs)</label>
              <Form.Input
                name="duracion"
                value={turno?.duracion}
                // onChange={formik.handleChange}
              />
            </div>
            <div class="field">
              <label>Fecha</label>
              <Form.Input
                name="fecha"
                value={formik.values.fecha}
                // onChange={formik.handleChange}
                error={formik.errors.fecha}
              />
            </div>
          </div>
        </div>
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
      <h4 className="ui dividing header">Personal Asignado a la vigilancia</h4>

      {/* <div class="three fields">
         
            <div class="field">
              <label>Legajo</label>
              <div class="field">
                <Form.Select
                  search
                  name={`Turnos[0].legajo`}
                  options={recursos}
                  placeholder="Buscar Legajo"
                  value={formik.values.Turnos[0].legajo}
                  onChange={(_, data) =>
                    formik.setFieldValue(`Turnos[0].legajo`, data.value)
                  }
                />
              </div>
            </div>
      
         
            <div class="field">
              <label>Nombre y Apellido</label>
              <div class="field">
                <Form.Input
                  name={`Turnos[0].nombre`}
                  placeholder="Nombre y Apellido"
                  value={formik.values.Turnos[0].nombre}
                  onChange={formik.handleChange}
                  error={formik.errors.Turnos?.nombre}
                />
              </div>
            </div>
          
         
            <div class="field">
              <label>Horario del turno</label>
              <div class="field">
                <Form.Select
                  search
                  name={`Turnos[0].turno`}
                  options={horariosOptions}
                  placeholder="Asignar Turno"
                  value={formik.values.Turnos[0].turno}
                  onChange={(_, data) =>
                    formik.setFieldValue(`Turnos[0].turno`, data.value)
                  }
                />
              </div>
            </div>
          
        </div> */}
      <div>
        <label>Ingrese la cantidad de Turnos de la vigilancia:</label>
        <div class="one field">
          <input
            type="number"
            min={1}
            max={6}
            placeholder="Ingrese la cantidad de personal para la vigilancia (MAXIMO 6)"
            value={numCampos}
            onChange={handleInputChange}
          />
        </div>
        <h4 className="ui dividing header">Personal</h4>
        {campos}
      </div>
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

function initialValues(
  fecha_inicio,
  fecha_fin,
  arreglo3,
  jurisdiccion,
  servicio,
  fechaFormateada,
  numCampos
) {
  return {
    jurisdiccion: jurisdiccion,
    tipo_servicio: servicio,
    fecha_inicio: fecha_inicio,
    fecha_fin: fecha_fin,
    Turnos: arreglo3,
    fecha: fechaFormateada,
    numCampos,
  };
}

function validationSchema() {
  return {
    // password: Yup.string().required(true),
    // nuevacontraseña: Yup.string().required(true),
  };
}

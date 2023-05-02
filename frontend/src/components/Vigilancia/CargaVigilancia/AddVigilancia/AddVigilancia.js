import React, { useState ,useEffect} from "react";
import { Button, Form, Icon,Checkbox } from "semantic-ui-react";
import {useVigilancia,useAuth} from "../../../../hooks"
import {MapView} from "../../Mapa/react-leaflet"
import { useFormik } from "formik";
import * as Yup from "yup";
// import { useAuth} from "../../hooks";
import { toast, Flip } from "react-toastify";
import Swal from "sweetalert2";
import "./AddVigilancia.scss"
export function AddVigilancia(props) {
     const [position,setposition]=useState({ lat:  -24.09804180450979, lng:-65.07202148437501 });
     const {addHorarios}=props;
     const {auth} = useAuth();
     const [formHorario,setformHorario] = useState(null)
     const {addVigilancia,get_jurisdicciones} = useVigilancia()
    // const {auth}=useAuth();
    // const {actualizar_contra,actualizar_contra_admin} =useContrasena();
    const motivos = [
      { key: "1", text: "Violencia de genero", value: 1 },
      { key: "2", text: "Edificio Publico", value: 2 },
      { key: "3", text: "Funcionarios Publicos", value: 3 },
      { key: "4", text: "Proteccion de Personas", value: 4 },]
    
      const servicios = [
        { key: "1", text: "Vigilancia de externa", value: 1 },
        { key: "2", text: "Vigilancia interna", value: 2 },
        { key: "3", text: "Custodia de Bienes", value: 3 },
        { key: "4", text: "Custodia de Detenidos", value: 4 },
        { key: "5", text: "Vigilancia de Persona", value: 5 }]

        const recursos = [
          { key: "1", text: "Auto", value: 1 },
          { key: "2", text: "Camioneta", value: 2 },
          { key: "3", text: "Moto", value: 3 },
          { key: "4", text: "Bicicleta", value: 4 },
          { key: "5", text: "Equino", value: 5 },
          { key: "6", text: "Carpa Azul", value: 6 },
          { key: "7", text: "Canes", value: 7 },
          { key: "8", text: "Otro", value: 8 }]

          const regionales = [
            { key: "1", text: "URR 1", value: "1" },
            { key: "2", text: "URR 2", value: "2" },
            { key: "3", text: "URR 3", value: "3" },
            { key: "4", text: "URR 4", value: "4" },
            { key: "5", text: "URR 5", value: "5" },
            { key: "6", text: "URR 6", value: "6" },
            { key: "7", text: "URR 7", value: "7" },
            { key: "8", text: "URR 8", value: "8" }]


            const [franja, setFranja] = useState(null);
            useEffect(() => {
              if(auth.usuario.unidad_regional===null){
                buscarJurisdicciones(0)
              }else{
                buscarJurisdicciones(auth.usuario.unidad_regional)
              }
            
            }, []);
            
            const buscarJurisdicciones = async (id) => {
              const options = await get_jurisdicciones(id);
              
              setFranja(options.map((option) => option));
            };
      const valores = franja?.map((tipo, index) => ({
        value:tipo.id,
        key: `${index}`,
        text: tipo.jurisdiccion,
      }));
  const formik = useFormik({
    initialValues: initialValues(auth),
    validationSchema: Yup.object(validationSchema()),
    onSubmit: async (formValue) => {
      try {
        const objeto={
          fk_jurisdiccion: formValue.juridiccion,
         fk_motivo:formValue.motivo,
         fk_tipo_servicio:formValue.tipo_servicio,
         fk_tipo_recurso:formValue.recursos,
         fk_unidad_regional:formValue.regional,
         objetivo:formValue.objetivo,
         cant_dias:0,
         fecha_inicio:formValue.fecha_inicio,
         fecha_fin: formValue.fecha_fin,
         destino:formValue.destino,
         latitud:position.lat.toFixed(6),
         longitud:position.lng.toFixed(6),}
        if(formValue.fecha_indefinida===true){
          objeto.fecha_fin=null
         }

         console.log(formHorario)
         console.log(objeto)
         console.log(valores)
         const response = await addVigilancia(objeto)
          
        if(response.msj){
        Swal.fire({
          title: "Exito!",
          text: response.msj,
          icon: "success",
          timer: 3000,
          showConfirmButton: true,
        });
        window.location.replace("http://localhost:3000/admin/vigilancia");
      }else{
        Swal.fire({
          title: "Algunos datos ingresados no son validos!",
          text: response.msj,
          icon: "error",
          showConfirmButton: true,
        });
    
    }
      } catch (error) {
      
        toast.error(error.message);
      }
    },
  });

  return (
    <Form className="ui form custom-form" onSubmit={formik.handleSubmit}>
      {auth?.usuario?.rol===3 &&
      <div className="field">
        <label>Regional</label>
        <div className="disable">
        <Form.Input
            name="regional"
            value={formik.values.regional}
            // placeholder={`UNIDAD REGIONAL ${formik.values.regional}`}
            // onChange={formik.handleReset}
            error={formik.errors.regional}
          />
          </div>
      </div>
    }
     {auth?.usuario?.rol===1 &&
       <div className="field">
        <label>Regional</label>
        
        <Form.Select
          fluid
          name="regional"
          options={regionales}
          placeholder="Seleccione la regional"
          value={formik.values.regional}
          onChange={(_, data) => formik.setFieldValue("regional", data.value)}
        />
          
      </div>
}
      <div className="two fields">
        <div className="field">
          <label>Juridiccion</label>
          <Form.Select
            search
            name="juridiccion"
            options={valores? valores:0}
            placeholder="Seleccione la juridiccion"
            value={formik.values.juridiccion}
            onChange={(_, data) =>
              formik.setFieldValue("juridiccion", data.value)
            }
          />
        </div>
        <div className="field">
          <label>Motivo</label>
          <div className="field">
            <Form.Select
              name="motivo"
              options={motivos}
              placeholder="Seleccione el motivo"
              value={formik.values.motivo}
              onChange={(_, data) => formik.setFieldValue("motivo", data.value)}
            />
          </div>
        </div>
      </div>
      <div className="field">
        <label>Tipo Servicio</label>
        <div className="fields">
          <Form.Select
            name="tipo_servicio"
            options={servicios}
            placeholder="Seleccione el tipo de servicio "
            value={formik.values.tipo_servicio}
            onChange={(_, data) =>
              formik.setFieldValue("tipo_servicio", data.value)
            }
          />
        </div>
      </div>
      <div className="two fields">
        <div className="field">
          <label>Objetivo</label>
          <Form.TextArea
            name="objetivo"
            placeholder="Escriba un objetivo"
            value={formik.values.objetivo}
            onChange={formik.handleChange}
            error={formik.errors.objetivo}
          />
        </div>
       
      </div>
      <h4 className="ui dividing header">Fechas de Vigilancia</h4>
      <div className="two fields">
        <div className="field">
          <label>Fecha de inicio</label>
          <Form.Input
            name="fecha_inicio"
            type="date"
            value={formik.values.fecha_inicio}
            onChange={formik.handleChange}
            error={formik.errors.fecha_inicio}
          />
        </div>
        <div className="two fields">
          {formik.values.fecha_indefinida === false && (
            <div className="field">
              <label>Fecha fin de vigilancia</label>
              <Form.Input
                name="fecha_fin"
                type="date"
                value={formik.values.fecha_fin}
                onChange={formik.handleChange}
                error={formik.errors.fecha_fin}
              />
            </div>
          )}
          <div className="field">
            <label>Fecha de fin de vigilancia indefinida</label>
            <div className="field">
              <div className="add-edit-user-form__staff">
                <Checkbox
                  toggle
                  checked={formik.values.fecha_indefinida}
                  onChange={(_, data) => {
                    formik.setFieldValue("fecha_indefinida", data.checked);
                  }}
                />{" "}
                Indefinida
              </div>
            </div>
          </div>
        </div>
      </div>
     
      <h4 className="ui dividing header">Recursos</h4>
      <div className="two fields">
        <div className="field">
          <label>Destino</label>
          <Form.Input
            name="destino"
            placeholder="Indique el destino"
            value={formik.values.destino}
            onChange={formik.handleChange}
            error={formik.errors.destino}
          />
        </div>
        <div className="field">
          <label>Recursos</label>
          <div className="field">
            <Form.Select
              name="recursos"
              options={recursos}
              placeholder="Seleccione los recursos "
              value={formik.values.recursos}
              onChange={(_, data) =>
                formik.setFieldValue("recursos", data.value)
              }
            />
          </div>
        </div>
      </div>
      <h4 className="ui dividing header">Ubicacion de la vigilancia</h4>
      <div className="two fields">
        <MapView 
         position={position}
         setposition={setposition}
         />
       
      </div>
      <div className="boton_crear_vigilancia">
        <Button
          className="positive button"
          type="submit"
          content={"Crear Vigilancia"}
        />
      </div>
    </Form>
  );
}

function initialValues(auth) {
  return {
    regional:auth?.usuario?.rol===3?  auth.usuario.unidad_regional:"",
    juridiccion: "",
    motivo:"",
    tipo_servicio:"",
    objetivo:"",
    cantidad_dias:0,
    fecha_inicio:"",
    fecha_fin: null,
    fecha_indefinida:false,
    // hora_inicio:"",
    // hora_fin:"",
    destino:"",
    recursos:"",
    latitud:"",
    longitud:"",
  };
}

function validationSchema() {
  return {
    // juridiccion: Yup.number().required("Seleccione una Juridiccion"),
    // motivo: Yup.number().required("Seleccione un Motivo"),
    // tipo_servicio: Yup.number().required("Seleccione un Tipo de Servicio"),
    // Objetivo:Yup.string().required("Escriba un objetivo para la vigilancia"),
    // fecha_inicio: Yup.date().required("La fecha de inicio es requerida"),
    // destino: Yup.string().required("Escriba un destino"),
    // recursos: Yup.number().required("Seleccione un recurso")

  };
}

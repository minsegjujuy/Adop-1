import React, { useState } from "react";
import "./AddVigilancia.scss";
import { Button, Form, Icon,Checkbox } from "semantic-ui-react";
import {useVigilancia} from "../../../../hooks"
import { useFormik } from "formik";
import * as Yup from "yup";
// import { useAuth} from "../../hooks";
import { toast, Flip } from "react-toastify";
import Swal from "sweetalert2";

export function AddVigilancia(props) {
     const {addHorarios}=props;
     const [formHorario,setformHorario] = useState(null)
     const {addVigilancia} = useVigilancia()
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
        { key: "4", text: "Vigilancia de Persona", value: 5 }]

        const recursos = [
          { key: "1", text: "Auto", value: 1 },
          { key: "2", text: "Camioneta", value: 2 },
          { key: "3", text: "Moto", value: 3 },
          { key: "4", text: "Bicicleta", value: 4 },
          { key: "5", text: "Equino", value: 5 },
          { key: "6", text: "Carpa Azul", value: 6 },
          { key: "7", text: "Canes", value: 7 },
          { key: "8", text: "Otro", value: 8 }]
  


      // const options = options3?.map((tipo, index) => ({
      //   value: tipo.value,
      //   key: `${tipo} ${index}`,
      //   text: tipo.text,
      // }));
  const formik = useFormik({
    initialValues: initialValues(),
    validationSchema: Yup.object(validationSchema()),
    onSubmit: async (formValue) => {
      try {
        const objeto={
          fk_juridiccion: formValue.juridiccion,
         fk_motivo:formValue.motivo,
         fk_servicio:formValue.tipo_servicio,
         objetivo:formValue.objetivo,
         cant_dias:0,
         fecha_inicio:formValue.fecha_inicio,
         fecha_fin: formValue.fecha_fin,
         destino:formValue.destino,
         recursos:formValue.recursos,
         latitud:formValue.latitud,
         longitud:formValue.longitud,}
        if(formValue.fecha_indefinida===true){
          objeto.fecha_fin=null
         }

         console.log(formHorario)
         console.log(objeto)
         const response = await addVigilancia(objeto)
    //    if(formValue.aux===formValue.nuevacontraseña){
    //     if(comando==="contra"){
    //       const form2 = {
    //         nuevaContraseña:formValue.nuevacontraseña,
    //       }
          
    //       const response = await actualizar_contra_admin(idUser,form2)
    //       if(response.msj==="Contraseña actualizada correctamente"){
    //         Swal.fire({
    //           title: "Exito!",
    //           text: response.msj,
    //           icon: "success",
    //           timer: 3000,
    //           showConfirmButton: true,
    //         });
    //         onClose()
    //       }else{
    //         Swal.fire({
    //           title: "Algunos datos ingresados no son validos!",
    //           text: response.msj,
    //           icon: "error",
    //           showConfirmButton: true,
    //         });
    //       }
    //     }else{
    //     const nuevo = {
    //       password:formValue.password,
    //       nuevaContraseña:formValue.nuevacontraseña,
    //     }
    //     const id = formValue.id
    //     const response= await actualizar_contra(id,nuevo)
    //     if(response.msj==="Contraseña actualizada correctamente"){
    //     Swal.fire({
    //       title: "Exito!",
    //       text: response.msj,
    //       icon: "success",
    //       timer: 3000,
    //       showConfirmButton: true,
    //     });
    //     window.location.reload();
    //   }else{
    //     Swal.fire({
    //       title: "Algunos datos ingresados no son validos!",
    //       text: response.msj,
    //       icon: "error",
    //       showConfirmButton: true,
    //     });
    //   }
    // }
    // }
      } catch (error) {
      
        toast.error(error.message);
      }
    },
  });

  return (
    <Form class="ui form" onSubmit={formik.handleSubmit}>
   <div class="two fields">
    <div class="field">
      <label>Juridiccion</label>
      <Form.Input
        name="juridiccion"
        type="number"
        placeholder="Ingrese la juridiccion"
        value={formik.values.juridiccion}
        onChange={formik.handleChange}
        error={formik.errors.juridiccion}
      />
        
    </div>
    <div class="field">
      <label>Motivo</label>
      <div class="field">
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
  <div class="field">
    <label>Tipo Servicio</label>
    <div class="fields">
    <Form.Select
        name="tipo_servicio"
        options={servicios}
        placeholder="Seleccione el tipo de servicio "
        value={formik.values.tipo_servicio}
        onChange={(_, data) => formik.setFieldValue("tipo_servicio", data.value)}
      />
    </div>
  </div>
  <div class="two fields">
    <div class="field">
      <label>Objetivo</label>
      <Form.TextArea
       name="objetivo"
       placeholder="Escriba un objetivo"
       value={formik.values.objetivo}
       onChange={formik.handleChange}
        error={formik.errors.objetivo}
      />
        
    </div>
    <div class="two fields">
       <div class="field">
      <label>Cantidad de dias</label>
      <Form.Input
       name="cantidad_dias"
       type="number"
       placeholder="Escriba la cantidad"
       value={formik.values.cantidad_dias}
       onChange={formik.handleChange}
        error={formik.errors.cantidad_dias}
      />
        
    </div>
    <div class="field">
      <label>Asignar turnos</label>
      <div class="field">
       <Button className="pencil alternate" positive onClick={()=>addHorarios(formik.values.cantidad_dias,setformHorario)}>
        <Icon className="pencil alternate"/>
        </Button>
       </div>
    </div>
  </div>
  </div>
  <h4 class="ui dividing header">Fechas de Vigilancia</h4>
  <div class="two fields">
    <div class="field">
      <label>Fecha de inicio</label>
      <Form.Input
       name="fecha_inicio"
       type="date"
       value={formik.values.fecha_inicio}
       onChange={formik.handleChange}
        error={formik.errors.fecha_inicio}
      />
        
    </div>
    <div class="two fields">
    {formik.values.fecha_indefinida===false &&
    <div class="field">
      
      <label>Fecha fin de vigilancia</label>
      <Form.Input
       name="fecha_fin"
       type="date"
       value={formik.values.fecha_fin}
       onChange={formik.handleChange}
        error={formik.errors.fecha_fin}
      />

    </div>
}
    <div class="field">
      <label>Fecha de fin de vigilancia indefinida</label>
      <div class="field">
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
  {/* <div class="two fields">
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
  </div> */}
  <h4 class="ui dividing header">Personal</h4>
  <div class="two fields">
    <div class="field">
      <label>Destino</label>
      <Form.Input
        name="destino"
        placeholder="Indique el destino"
        value={formik.values.destino}
        onChange={formik.handleChange}
        error={formik.errors.destino}
      />
        
    </div>
    <div class="field">
      <label>Recursos</label>
      <div class="field">
      <Form.Select
        name="recursos"
        options={recursos}
        placeholder="Seleccione los recursos "
        value={formik.values.recursos}
        onChange={(_, data) => formik.setFieldValue("recursos", data.value)}
      />
        
       </div>
    </div>
  </div>
  <h4 class="ui dividing header">Ubicacion de la vigilancia</h4>
  <div class="two fields">
    <div class="field">
      <label>Latitud</label>
      <Form.Input
        name="latitud"
        type="double"
        placeholder="Indique latitud"
        value={formik.values.latitud}
        onChange={formik.handleChange}
        error={formik.errors.latitud}
      />
    </div>
    <div class="field">
      <label>Longitud</label>
      <div class="field">
      <Form.Input
        name="longitud"
        type="double"
        placeholder="Indique longitud"
        value={formik.values.longitud}
        onChange={formik.handleChange}
        error={formik.errors.longitud}
      />
        
       </div>
    </div>
  </div>
  <div className="boton_crear_vigilancia">
  <Button className="positive button" type="submit" content={"Crear Vigilancia"}  />
  </div>
</Form>
  );
}

function initialValues() {
  return {
    juridiccion: "",
    motivo:"",
    tipo_servicio:"",
    objetivo:"",
    cantidad_dias:"",
    fecha_inicio:"01/01/2010",
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
    // password: Yup.string().required(true),
    // nuevacontraseña: Yup.string().required(true),
  };
}

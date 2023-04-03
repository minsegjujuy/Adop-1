import React, { useState } from "react";
import "./AddVigilancia.scss";
import { Button, Form, Icon,Checkbox } from "semantic-ui-react";
import { useFormik } from "formik";
import * as Yup from "yup";
// import { useAuth} from "../../hooks";
import { toast, Flip } from "react-toastify";
import Swal from "sweetalert2";

export function AddVigilancia(props) {
     const {addHorarios}=props;
     const [formHorario,setformHorario] = useState(null)
    // const {auth}=useAuth();
    // const {actualizar_contra,actualizar_contra_admin} =useContrasena();
    const motivos = [
      { key: "1", text: "Violencia de genero", value: "Violencia de genero" },
      { key: "2", text: "Edificio Publico", value: "Edificio Publico" },
      { key: "3", text: "Funcionarios Publicos", value: "Funcionarios Publicos" },
      { key: "4", text: "Proteccion de Personas", value: "Proteccion de Personas" },]
    
      const servicios = [
        { key: "1", text: "Vigilancia de externa", value: "Vigilancia externa" },
        { key: "2", text: "Vigilancia interna", value: "Vigilancia interna" },
        { key: "3", text: "Custodia de Bienes", value: "Custodia de Bienes" },
        { key: "4", text: "Custodia de Detenidos", value: "Custodia de Detenidos" },]

        const recursos = [
          { key: "1", text: "Auto", value: "Auto" },
          { key: "2", text: "Camioneta", value: "Camioneta" },
          { key: "3", text: "Moto", value: "Moto" },
          { key: "4", text: "Bicicleta", value: "Bicicleta" },
          { key: "5", text: "Equino", value: "Equino" },
          { key: "6", text: "Carpa Azul", value: "Carpa Azul" },
          { key: "7", text: "Canes", value: "Canes" },
          { key: "8", text: "Otro", value: "Otro" }]
  


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
         console.log(formHorario)
         console.log(formValue)
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
  <div class="two fields">
    <div class="field">
      <label>Hora de inicio</label>
      <Form.Input
        name="hora_inicial"
        type="time"
        placeholder="Ingrese hora inicial"
        value={formik.values.hora_inicial}
        onChange={formik.handleChange}
        error={formik.errors.hora_inicial}
      />
        
    </div>
    <div class="field">
      <label>Hora final</label>
      <div class="field">
      <Form.Input
        name="hora_final"
        type="time"
        placeholder="Ingrese hora final"
        value={formik.values.hora_final}
        onChange={formik.handleChange}
        error={formik.errors.hora_final}
      />
        
       </div>
    </div>
  </div>
  <h4 class="ui dividing header">Personal</h4>
  <div class="two fields">
    <div class="field">
      <label>Personal Afectado</label>
      <Form.Input
        name="personal_afectado"
        type="number"
        placeholder="Indique la cantidad de personal afectado"
        value={formik.values.personal_afectado}
        onChange={formik.handleChange}
        error={formik.errors.personal_afectado}
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
    hora_inicio:"",
    hora_fin:"",
    personal_afectado:"",
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

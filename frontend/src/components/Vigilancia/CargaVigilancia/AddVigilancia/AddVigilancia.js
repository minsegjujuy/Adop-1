import React from "react";
import "./AddVigilancia.scss";
import { Button, Form } from "semantic-ui-react";
import { useFormik } from "formik";
import * as Yup from "yup";
// import { useAuth} from "../../hooks";
import { toast, Flip } from "react-toastify";
import Swal from "sweetalert2";

export function AddVigilancia(props) {
    // const {onClose,onRefetch,idUser,comando}=props;
    // const {auth}=useAuth();
    // const {actualizar_contra,actualizar_contra_admin} =useContrasena();
    const options = [
      { key: "operador", text: "Operador", value: "operador" },
      { key: "Administrador", text: "Administrador", value: "administrador" },
      { key: "General", text: "General", value: "general" },]

  const formik = useFormik({
    initialValues: initialValues(),
    validationSchema: Yup.object(validationSchema()),
    onSubmit: async (formValue) => {
      try {
       
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
        options={options}
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
        options={options}
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
    <div class="field">
      <label>Cantidad de dias</label>
      <div class="field">
      <Form.Input
       name="cantidad_dias"
       type="number"
       placeholder="Escriba un objetivo"
       value={formik.values.cantidad_dias}
       onChange={formik.handleChange}
        error={formik.errors.cantidad_dias}
      />
        
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
    <div class="field">
      <label>Fecha fin de vigilancia</label>
      <div class="field">
      <Form.Input
       name="fecha_fin"
       type="date"
       value={formik.values.fecha_fin}
       onChange={formik.handleChange}
        error={formik.errors.fecha_fin}
      />
        
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
        options={options}
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
  
  <Button type="submit" primary fluid content={"Crear Vigilancia"} />
</Form>
  );
}

function initialValues(id,comando) {
  return {
    nuevacontraseña: "",
    aux:"",
    password:"",
    id:"",

  };
}

function validationSchema() {
  return {
    password: Yup.string().required(true),
    nuevacontraseña: Yup.string().required(true),
  };
}

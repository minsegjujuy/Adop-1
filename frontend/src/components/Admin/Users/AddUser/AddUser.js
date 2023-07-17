import { useFormik } from "formik";
import { Form, Button,Checkbox} from "semantic-ui-react";
import {useUser,useVigilancia} from "../../../../hooks/";
import {useState,useEffect} from "react"
import Swal from "sweetalert2";
import "./AddUser.scss"
import * as Yup from "yup";

export const AddUser= (props) => {
  const {
    onClose,
    Refetch,
  } = props;

   const {addUser,auth} = useUser();
   const {get_jurisdicciones} = useVigilancia();
   const options = [
    { key: "Administrador", text: "Administrador", value: 1 },
    { key: "General", text: "General", value: 2 },
    { key: "operador", text: "Operador", value: 3 },
    
   
  ];
  const options2 = [
    { key: "Regional 1", text: "Regional 1", value: 1 },
    { key: "Regional 2", text: "Regional 2", value: 2 },
    { key: "Regional 3", text: "Regional 3", value: 3 },
    { key: "Regional 4", text: "Regional 4", value: 4 },
    { key: "Regional 5", text: "Regional 5", value: 5 },
    { key: "Regional 6", text: "Regional 6", value: 6 },
    { key: "Regional 7", text: "Regional 7", value: 7 },
    { key: "Regional 8", text: "Regional 8", value: 8 },
  ];
  const [franja, setFranja] = useState(null);
  useEffect(() => {
      buscarJurisdicciones(0)
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
    initialValues: initialValues(),
    validationSchema: Yup.object(newSchema()),
    validateOnChange: false,
    onSubmit: async (formValue) => {
    //   formValue.nombres = formValue.nombres.toUpperCase();
    //   formValue.apellidos = formValue.apellidos.toUpperCase();
    console.log(formValue)
      try {
        
        if(formValue.rol===1){
          formValue.is_superuser = true
        }else{
          formValue.is_superuser=false
        }
        console.log(formValue)
        Swal.fire({
          icon: "info",
          title: "Creando Empleado",
          text: "El Empleado se esta creando, aguarde un instate...",
          showConfirmButton: false,
          showLoaderOnConfirm: true,
          didOpen: () => {
            Swal.showLoading();
          },
        });
        const resultado = await addUser(formValue);
        console.log(resultado)
        if (resultado.msj) {
          Swal.fire({
            title: "Individuo agregado Correctamente!",
            text: resultado.msj,
            icon: "success",
            timer: 3000,
            showConfirmButton: true,
          });
          onClose();
          window.location.reload();
        } else {
          Swal.fire({
            title: "Algunos datos ingresados no son validos!",
            text: "Revise los campos indicados e ingreselos correctamente",
            icon: "error",
            showConfirmButton: true,
          });
        }
      } catch (error) {
        
      }
    },
  });

  return (
    <Form className="add-edit-user-form" onSubmit={formik.handleSubmit}>
      <Form.Select
        name="unidad_regional"
        options={options2}
        placeholder="Seleccione la regional "
        value={formik.values.unidad_regional}
        onChange={(_, data) => formik.setFieldValue("unidad_regional", data.value)}
      />
      <Form.Select
        name="jurisdiccion"
        options={valores}
        placeholder="Seleccione la juridiccion "
        value={formik.values.jurisdiccion}
        onChange={(_, data) => formik.setFieldValue("jurisdiccion", data.value)}
      />
      <Form.Input
        name="username"
        placeholder="Ingrese un nombre de usuario"
        value={formik.values.username}
        onChange={formik.handleChange}
        error={formik.errors.username}
      />
      <Form.Input
        name="email"
        placeholder="Ingrese un Correo electronico"
        value={formik.values.email}
        onChange={formik.handleChange}
        error={formik.errors.email}
      />
      <Form.Input
        name="nombres"
        placeholder="Ingrese su nombre "
        value={formik.values.nombres}
        onChange={formik.handleChange}
        error={formik.errors.nombres}
      />
      <Form.Input
        name="apellidos"
        placeholder="Ingrese su apellido"
        value={formik.values.apellidos}
        onChange={formik.handleChange}
        error={formik.errors.apellidos}
      />
      <Form.Input
        name="password"
        placeholder="Ingrese una Contraseña"
        type="password"
        value={formik.values.password}
        onChange={formik.handleChange}
        error={formik.errors.password}
      />
      <Form.Select
        name="rol"
        options={options}
        placeholder="Seleccione el tipo de permiso"
        value={formik.values.rol}
        onChange={(_, data) => formik.setFieldValue("rol", data.value)}
      />
      {/* {formik.values.rol==="administrador" &&
      <div className="add-edit-user-form__staff">
        <Checkbox
          toggle
          checked={formik.values.is_superuser}
          onChange={(_, data) => {
            formik.setFieldValue("is_superuser", data.checked);
          }}
        />{" "}
        Usuario Staff (Debe tildar la opcion staff)
        </div>
      } */}
      <Button type="submit" primary fluid content={"Crear Usuario"} />
    </Form>
  );
};

 function initialValues() {
  return {
    unidad_regional:"",
    jurisdiccion:"",
    username:"",
    email: "",
    nombres: "",
    apellidos: "",
    password:"",
    rol: "",
    is_superuser:false,
          // usuario_activo: true,
          // is_superuser: false,
        }
          

      }

 function newSchema() {
  return {
    // user:{username:Yup.string(),
    // email: Yup.string().email(true).required(true),
    // first_name: Yup.string().required(true),
    // last_name: Yup.string().required(true),
    // password: Yup.string().required(true),
    // is_staff: Yup.bool().required(true),
    // is_active: Yup.bool().required(true),},
    // nivel_permiso : Yup.string().required
  };
 }

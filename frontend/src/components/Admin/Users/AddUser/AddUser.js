import { useFormik } from "formik";
import { Form, Button,Checkbox} from "semantic-ui-react";
import {useUser} from "../../../../hooks/";
import Swal from "sweetalert2";
import "./AddUser.scss"
import * as Yup from "yup";

export const AddUser= (props) => {
  const {
    onClose,
    Refetch,
  } = props;

   const {addUser} = useUser();
   const options = [
    { key: "operador", text: "Operador", value: "operador" },
    { key: "Administrador", text: "Administrador", value: "administrador" },
    { key: "General", text: "General", value: "general" },
    
   
  ];
  const formik = useFormik({
    initialValues: initialValues(),
    validationSchema: Yup.object(newSchema()),
    validateOnChange: false,
    onSubmit: async (formValue) => {
    //   formValue.nombres = formValue.nombres.toUpperCase();
    //   formValue.apellidos = formValue.apellidos.toUpperCase();
      try {
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
        if (resultado.id) {
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
      <Form.Input
        name="User.username"
        placeholder="Ingrese un nombre de usuario"
        value={formik.values.User?.username}
        onChange={formik.handleChange}
        error={formik.errors.User?.username}
      />
      <Form.Input
        name="User.email"
        placeholder="Ingrese un Correo electronico"
        value={formik.values.User?.email}
        onChange={formik.handleChange}
        error={formik.errors.User?.email}
      />
      <Form.Input
        name="User.first_name"
        placeholder="Ingrese su nombre "
        value={formik.values.User?.first_name}
        onChange={formik.handleChange}
        error={formik.errors.User?.first_name}
      />
      <Form.Input
        name="User.last_name"
        placeholder="Ingrese su apellido"
        value={formik.values.User?.last_name}
        onChange={formik.handleChange}
        error={formik.errors.User?.last_name}
      />
      <Form.Input
        name="User.password"
        placeholder="Ingrese una Contraseña"
        type="password"
        value={formik.values.User?.password}
        onChange={formik.handleChange}
        error={formik.errors.User?.password}
      />
      <div className="add-edit-user-form__staff">
        <Checkbox
          toggle
          checked={formik.values.User?.is_staff}
          onChange={(_, data) => {
            formik.setFieldValue("User.is_staff", data.checked);
          }}
        />{" "}
        Usuario Staff
        </div>
      <Form.Select
        name="nivel_permiso"
        options={options}
        placeholder="Seleccione el tipo de permiso"
        value={formik.values.nivel_permiso}
        onChange={(_, data) => formik.setFieldValue("nivel_permiso", data.value)}
      />

      <Button type="submit" primary fluid content={"Crear Usuario"} />
    </Form>
  );
};

 function initialValues() {
  return {
    User:{username:"",
          email: "",
          first_name: "",
          last_name: "",
          password:"",
          is_active: false,
          is_staff: false,},
    nivel_permiso: ""

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

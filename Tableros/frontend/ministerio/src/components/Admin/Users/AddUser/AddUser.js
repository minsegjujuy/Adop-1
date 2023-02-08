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
          title: "Creando Individuo",
          text: "El Individuo se esta creando, aguarde un instate...",
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
        name="first_name"
        placeholder="Ingrese su nombre "
        value={formik.values.first_name}
        onChange={formik.handleChange}
        error={formik.errors.first_name}
      />
      <Form.Input
        name="last_name"
        placeholder="Ingrese su apellido"
        value={formik.values.last_name}
        onChange={formik.handleChange}
        error={formik.errors.last_name}
      />
      <Form.Input
        name="password"
        placeholder="Ingrese una Contraseña"
        type="password"
        value={formik.values.password}
        onChange={formik.handleChange}
        error={formik.errors.password}
      />
      <div className="add-edit-user-form__staff">
        <Checkbox
          toggle
          checked={formik.values.is_staff}
          onChange={(_, data) => {
            formik.setFieldValue("is_staff", data.checked);
          }}
        />{" "}
        Usuario Administrador
        </div>
      {/* <Form.Select
        name="sexo"
        options={options}
        placeholder="Seleccione Sexo"
        value={formik.values.sexo}
        onChange={(_, data) => formik.setFieldValue("sexo", data.value)}
      /> */}

      <Button type="submit" primary fluid content={"Crear Usuario"} />
    </Form>
  );
};

 function initialValues() {
  return {
    username:"",
    email: "",
    first_name: "",
    last_name: "",
    password:"",
    is_active: false,
    is_staff: false,
 }
}
 function newSchema() {
  return {
    username:Yup.string(),
    email: Yup.string().email(true).required(true),
    first_name: Yup.string().required(true),
    last_name: Yup.string().required(true),
    password: Yup.string().required(true),
    is_staff: Yup.bool().required(true),
    is_active: Yup.bool().required(true),
  };
 }

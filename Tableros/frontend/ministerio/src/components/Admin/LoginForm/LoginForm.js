import React, { useState } from "react";
import "./LoginForm.scss";
import { Button, Form} from "semantic-ui-react";
import { useFormik } from "formik";
import * as Yup from "yup";
import { loginApi } from "../../../api/user";
import {useAuth} from "../../../hooks";
import { toast, Flip } from "react-toastify";

export function LoginForm() {
 const { login } = useAuth();

const [mostrarContrasenia, setMostrarContrasenia] = useState(false);

  const formik = useFormik({
    initialValues: initialValues(),
    validationSchema: Yup.object(validationSchema()),
    onSubmit: async (formValue) => {
      try {
        console.log(formValue)
        const response = await loginApi(formValue);
        const { access } = response;
        login(access);
        
        toast.success("Ingreso Exitoso", {
          position: toast.POSITION.BOTTOM_CENTER,
          autoClose: 2000,
          transition: Flip,
        });
      } catch (error) {
        toast.error(error.message);
      }
    },
  });

  return (
    <Form className="login-form-admin" onSubmit={formik.handleSubmit}>
      <Form.Input
        name="email"
        placeholder="Correo Electronico"
        value={formik.values.email}
        onChange={formik.handleChange}
        error={formik.errors.email}
      />
      <Form.Input
        name="password"
        placeholder="Contraseña"
        type={mostrarContrasenia ? "text" : "password"}
        value={formik.values.password}
        onChange={formik.handleChange}
        error={formik.errors.password}
        icon={{
          name: mostrarContrasenia ? "eye" : "eye slash",
          circular: true,
          link: true,
          onClick: () => {
            setMostrarContrasenia(!mostrarContrasenia);
          },
        }}
      />

      <Button type="submit" icon content="INICIAR SESION" primary fluid></Button>
    </Form>
  );
}

function initialValues() {
  return {
    email: "",
    password: "",
  };
}

function validationSchema() {
  return {
    email: Yup.string().email(true).required(true),
    password: Yup.string().required(true),
  };
}

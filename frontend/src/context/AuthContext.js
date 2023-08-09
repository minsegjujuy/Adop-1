import React, { useState, useEffect, createContext } from "react";
import { setToken } from "../api/token";
import { useUser } from "../hooks/useUser";
import { getToken, removeToken } from "../api/token";
import Swal from "sweetalert2";
import { logoutApi } from "../api/user";
// import { TOKEN, BASE_API } from "../utils/constants";

export const AuthContext = createContext({
  auth: null,
  // first:true,
  // first:1,
  login: () => null,
  logout: () => null,
});

export function AuthProvider(props) {
  const { children } = props;
  const [first, setfirst] = useState(1);
  const [auth, setAuth] = useState(JSON.parse(getToken()));
  const { getMeToken } = useUser();

  useEffect(() => {
    (async () => {
      let data = auth;
      // console.log(data)
      if (data) {
        const usuario = data?.usuario?.username;
        if (usuario) {
          var response = undefined;
          await getMeToken(usuario).then((token) => (response = token.token));
          if (response !== auth.token) {
            // TODO: Crear un modal que le pregunte al usuario si desea continuar con la sesion o directamente salir y deslogearse

            const newData = {
              token: response,
              usuario: data.usuario,
            };

            // console.log(newData)

            // let newData = {}
            // await getTokenApi(usuario).then((token)=> newData['token'] = token.token)
            // newData['usuario'] = JSON.stringify(data.usuario)

            setToken(JSON.stringify(newData));
          }
        } else {
          setAuth(null);
        }
      }
    })();
  }, [auth, getMeToken]);

  const logout = () => {
    if (auth) {
      removeToken();
      setAuth(null);
      logoutApi(auth.token);
      window.location.replace("http://localhost:3000/login");
    }
  };

  const login = async (response) => {
    const data = {
      token: response.token,
      usuario: {
        username: response.usuario.username,
        email: response.usuario.email,
        nombres: response.usuario.nombres,
        apellidos: response.usuario.apellidos,
        rol: response.usuario.rol,
        jurisdiccion: response.usuario.jurisdiccion,
        unidad_regional: response.usuario.unidad_regional,
      },
    };
    setToken(JSON.stringify(data));
    setAuth(JSON.stringify(data.token));
    // setTimeout(async function () {
    // const token = getToken();
    // if (token) {
    // const me = response.usuario;
    // if (me.code === "token_not_valid") {
    //   Swal.fire({
    //     icon: "info",
    //     iconColor: "lightblue",
    //     title: "Su sesion expiro",
    //     text: "su sesion expiro, inicie sesion nuevamente",
    //     showConfirmButton: true,
    //     confirmButtonText: "iniciar sesion",
    //     confirmButtonColor: "#3085d6",
    //     timer: 10000,
    //   }).then(async (result) => {
    //     if (result.isConfirmed) {
    //       window.location.reload();
    //     } else {
    //       window.location.reload();
    //     }
    //   });
    // }
    // }
    // }, 1810*1000);
    // console.log(response.token);

    //
  };

  const valueContext = {
    auth,
    first,
    setfirst,
    setAuth,
    login,
    logout,
  };

  if (auth === undefined) return null;

  return (
    <AuthContext.Provider value={valueContext}>{children}</AuthContext.Provider>
  );
}

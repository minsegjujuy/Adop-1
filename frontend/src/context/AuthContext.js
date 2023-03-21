import React, { useState, useEffect, createContext } from "react";
import { setToken } from "../api/token";
import { useUser } from "../hooks/useUser";
import { getToken, removeToken } from "../api/token";
import Swal from "sweetalert2";
import { getTokenApi, logoutApi } from "../api/user";
// import { TOKEN, BASE_API } from "../utils/constants";

export const AuthContext = createContext({
  auth: null,
  login: () => null,
  logout: () => null,
});

export function AuthProvider(props) {
  const { children } = props;
  const [auth, setAuth] = useState(JSON.parse(getToken()));
  // const [auth, setAuth] = useState(null);
  // const { getMe } = useUser();

  useEffect(() => {
    (async () => {
      let data = auth
      // console.log(data)
      if(data){
        const usuario = data?.usuario?.username;
        if (usuario) {
          // console.log(usuario)
          // let response
          // await getTokenApi(usuario).then((token)=> response = token)
          // const newData = {
          //   'token': await response.token,
          //   'usuario': JSON.stringify(data.usuario)
          // }
          // await console.log(newData)
          // console.log(JSON.parse(getToken()))
          // await setToken(JSON.stringify(newData));

        } else {
          setAuth(null);
        }
      }
    })();
  }, [auth]);

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
      'token': response.token,
      'usuario':{
        'username' : response.usuario.username,
        'email': response.usuario.email,
        'nombres': response.usuario.nombres,
        'apellidos': response.usuario.apellidos,
        'rol':response.usuario.rol
      }
    }
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
    
    window.location.replace("http://localhost:3000/admin/users");
  };

  const valueContext = {
    auth,
    login,
    logout,
  };

  if (auth === undefined) return null;

  return (
    <AuthContext.Provider value={valueContext}>{children}</AuthContext.Provider>
  );
}

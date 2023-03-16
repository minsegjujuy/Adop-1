import React, { useState, useEffect, createContext } from "react";
import { setToken } from "../api/token";
import { useUser } from "../hooks/useUser";
import { getToken, removeToken } from "../api/token";
import Swal from "sweetalert2";
// import { TOKEN, BASE_API } from "../utils/constants";

export const AuthContext = createContext({
  auth: null,
  login: () => null,
  logout: () => null,
});

export function AuthProvider(props) {
  const { children } = props;
  const [auth, setAuth] = useState(undefined);
  // const { getMe } = useUser();

  useEffect(() => {
    (async () => {
      const token = getToken();
      console.log(auth)
      if (token) {
        const me ={
          username: "Mauro",
          email:"maurocutipa18@gmail.com",
          nombres:"xxxxx",
          apellidos:"lalala",
          rol:"administrador"
        };;
        console.log(auth)
        if (me.code !== "token_not_valid") {
          setAuth({ token, me });
        } else {
          removeToken();
          setAuth(null);
        }
      } else {
        setAuth(null);
      }
    })();
  }, []);

  const logout = () => {
    if (auth) {
      window.location.replace("http://localhost:3000/");
      removeToken();
      setAuth(null);
    }
  };

  const login = async (response) => {
    console.log(response)
    setToken(response.token);
    const me = response.usuario;
    const token = response.token;
    setAuth(token,me);
    setTimeout(async function () {
      const token = getToken();
      if (token) {
        const me = response.usuario;
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
      }
    }, 1810*1000);
    console.log(response.token);
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

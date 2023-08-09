import React from "react";
import { useAuth } from "../../hooks/useAuth";

export function Home() {
  const { auth } = useAuth();
  const redireccionar = () => {
    if (auth)
      if (auth?.usuario?.rol === "administrador")
        window.location.replace("http://localhost:3000/admin/users");
      else window.location.replace("http://localhost:3000/admin/vigilancia");
    else window.location.replace("http://localhost:3000/login");
  };
  return redireccionar();
}

import React from "react";
import { BASE_APP } from "../../utils/contants";
import { useAuth } from "../../hooks/useAuth";

export function Home() {
  const { auth } = useAuth();
  const redireccionar = () => {
    if (auth)
      if (auth?.usuario?.rol === "administrador")
        window.location.replace(`${BASE_APP}/admin/users`);
      else window.location.replace(`${BASE_APP}/admin/vigilancia`);
    else window.location.replace(`${BASE_APP}/login`);
  };
  return redireccionar();
}

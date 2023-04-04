import {addVigilanciaApi} from "../api/vigilancia"
import { useState } from "react";
import {useAuth} from "../hooks"

export function useVigilancia() {
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState(null);
    const { auth } = useAuth();

      const addVigilancia = async (data) => {
        try {
          setLoading(true);
          const resultado = await addVigilanciaApi(data, auth.token);
          setLoading(false);
          return resultado;
        } catch (error) {
          setLoading(false);
          setError(error);
          
        }
      };
   
  // const buscarEmpleadoId = async (id) => {
  //   try {
  //     setLoading(true);
  //     const response = await buscarEmpleadoIdApi(id, auth.token);
  //     setLoading(false);
  //     return response;
  //   } catch (error) {
  //     setLoading(false);
  //     setError(error);
  //   }
  // };
    return {
        loading,
        error,
        addVigilancia,
        
       
    
    }
}
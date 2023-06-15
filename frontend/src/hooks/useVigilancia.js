import {addVigilanciaApi,getJurisdicciones,getVigilancias,addTurnosApi,getTurno,getPersonal,asignarPersonal,deleteVigilanciaApi} from "../api/vigilancia"
import { useState } from "react";
import {useAuth} from "../hooks"

export function useVigilancia() {
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState(null);
    const [vigilancias, setVigilancias] = useState(null);
    // const [personal, setPersonal] = useState(null);
    const [turno, setTurno]= useState(null);
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
      const get_jurisdicciones = async (id) => {
        try {
          setLoading(true);
          console.log(id)
          const resultado = await getJurisdicciones(auth.token,id);
          setLoading(false);
          return resultado;
        } catch (error) {
          setLoading(false);
          setError(error);
          
        }
      };
      const get_vigilancia = async (data) => {
        try {
          setLoading(true);
          const resultado = await getVigilancias(auth.token);
          setLoading(false);
          setVigilancias(resultado)
        } catch (error) {
          setLoading(false);
          setError(error);
          
        }
      };
      const add_turnos = async (data) => {
        try {
          setLoading(true);
          const resultado = await addTurnosApi(data, auth.token);
          setLoading(false);
          return resultado;
        } catch (error) {
          setLoading(false);
          setError(error);
          
        }
      };
      const get_turno = async (id) => {
        try {
          setLoading(true);
          const resultado = await getTurno(auth.token,id);
          setTurno(resultado)
          console.log(resultado)
          setLoading(false);
          
        } catch (error) {
          setLoading(false);
          setError(error);
          
        }
      };
      const get_personal = async (data) => {
        try {
          setLoading(true);
          const resultado = await getPersonal(auth.token);
          setLoading(false);
          return resultado
        } catch (error) {
          setLoading(false);
          setError(error);
          
        }
      };
      const asignar_personal = async (data,id) => {
        try {
          setLoading(true);
          const resultado = await asignarPersonal(data, auth.token,id);
          setLoading(false);
          return resultado
        } catch (error) {
          setLoading(false);
          setError(error);
          
        }
      };
      const deleteVigilancia = async (id) => {
        try {
          setLoading(true);
          await deleteVigilanciaApi(id, auth.token);
          setLoading(false);
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
        vigilancias,
        turno,
        auth,
        addVigilancia,
        get_jurisdicciones,
        get_vigilancia,
        add_turnos,
        get_turno,
        get_personal,
        asignar_personal,
        deleteVigilancia
        
        
       
    
    }
}
import { useState } from "react";
import { useAuth } from "./useAuth";

import {getMeApi,getUsersApi,addUserApi,deleteUserApi,buscarEmpleadoIdApi} from "../api/user"

export function useUser() {
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState(null);
    const [users, setUsers] = useState(null);
    const [empleado,setEmpleado] = useState(null)
    const { auth } = useAuth();

    const getMe = async (token) => {
        try {
          const response = await getMeApi(token);
          return response;
        } catch (error) {
          throw error;
        }
      };
    const getUsers = async () => {
        try {
          setLoading(true)
          const response = await getUsersApi(auth.token);
          // console.log(response)
          setLoading(false)
          setUsers(response)
        } catch (error) {
          setLoading(false)
          setError(error)
        }
      };
      const addUser = async (data) => {
        try {
          setLoading(true);
          const resultado = await addUserApi(data, auth.token);
          setLoading(false);
          return resultado;
        } catch (error) {
          setLoading(false);
          setError(error);
          
        }
      };
    const deleteUser = async (id) => {
    try {
      setLoading(true);
      await deleteUserApi(id, auth.token);
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
        users,
        setUsers,
        getMe,
        getUsers,
        addUser,
        deleteUser,
        // buscarEmpleadoId,
       
    
    }
}
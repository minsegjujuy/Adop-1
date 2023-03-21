import { useState } from "react";
import { useAuth } from "./useAuth";

import {getTokenApi,getUsersApi,addUserApi,deleteUserApi} from "../api/user"
import { setToken } from "../api/token";

export function useUser() {
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState(null);
    const [users, setUsers] = useState(null);
    const { auth } = useAuth();

    const getMeToken = async (usuario) => {
        try {
          let response
          await getTokenApi(usuario).then((token)=>response = token);
          return await response;
        } catch (error) {
          throw error;
        }
      };
    const getUsers = async () => {
        try {
          setLoading(true)
          const response = await getUsersApi(auth.token);
          // console.log(response);
          if(response.expired){
            let token
            await getMeToken(auth?.usuario?.username).then((value)=> token =value.token)
            const new_token={
              'token': await token,
              'usuario':auth?.usuario
            }
            await setToken(JSON.stringify(new_token))
            await getUsers();
          }
          else
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
        getMeToken,
        getUsers,
        addUser,
        deleteUser,
        // buscarEmpleadoId,
       
    
    }
}
import {BASE_API} from "../utils/contants"

export async function logoutApi(token){
  try{
    const url = `${BASE_API}/api/auth/logout/`
    const params = {
      method:"POST",
      headers:{
        "Content-Type":"application/json",
        "Authentication":token,
      },
      body: {"token": token,}
    }
    const response = await fetch(url,params);
    if(response.status !== 200){
      throw new Error(response.error)
    }
    const result = await response.json();

    return result;
    
  } catch(error){
    throw error
  }
}

export async function loginApi(formValue){
    try{
       const url =`${BASE_API}/api/auth/login/`
       const params={
        method:"POST",
        headers :{
            "Content-Type":"application/json",
        },
        body: JSON.stringify(formValue),
        
       }
       const response = await fetch(url, params);
       if (response.status !== 200) {
        throw new Error(response.error);
      }
      const result = await response.json();

      return result;
    }catch(error){
        throw error
    }

}

  export async function getTokenApi(usuario) {
    try {
      const url = `${BASE_API}/api/auth/refresh-token/?`+ new URLSearchParams({username:usuario});
      const response = await fetch(url);
      return await response.json();
    } catch (error) {
      throw error;
    }
  }

  export async function getUsersApi(token) {
    try {
      const url = `${BASE_API}/api/usuarios/`;
      const params = {
        headers: {
          Authorization: `Token ${token}`,
        },
      };
      const response = await fetch(url, params);
      const result = await response.json();
      return result;
    } catch (error) {
      throw error;
    }
  }
  export async function addUserApi(data, token) {
    try {
      const url = `${BASE_API}/api/usuarios/`;
      const params = {
        method: "POST",
        headers: {
          Authorization: `Token ${token}`,
          "Content-Type": "application/json",
        },
        body: JSON.stringify(data),
      };
  
      const response = await fetch(url, params);
      const result = await response.json();
      return result;
    } catch (error) {
      
      throw error;
    }
  }
  export async function deleteUserApi(id, token) {
    try {
      const url = `${BASE_API}/api/usuarios/${id}/`;
      const params = {
        method: "DELETE",
        headers: {
          Authorization: `Token ${token}`,
        },
      };
  
      const response = await fetch(url, params);
      const result = await response.json();
      return result;
    } catch (error) {
      throw error;
    }
  }
  // export async function buscarEmpleadoIdApi(id, token) {
  //   try {
  //     const url = `${BASE_API}/api/empleado_usuario/${id}/`;
  //     const params = {
  //       method: "GET",
  //       headers: {
  //         Authorization: `Bearer ${token}`,
  //       },
  //     };
  
  //     const response = await fetch(url, params);
  //     const result = await response.json();
  //     return result;
  //   } catch (error) {
  //     throw error;
  //   }
  // }
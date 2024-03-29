import {BASE_API} from "../utils/contants"

export async function addVigilanciaApi(data, token) {
    try {
      const url = `${BASE_API}/api/vigilancias/`;
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
  export async function getJurisdicciones(token,id) {
    try {
      const url = `${BASE_API}/api/dependencias/?uurr=${id}`;
      const params = {
        method: "GET",
        headers: {
          Authorization: `Token ${token}`,
        },
      };
      const response = await fetch(url, params);
      const result = await response.json();
      console.log(result);
      return result;
    } catch (error) {
      throw error;
    }
  }
  export async function getVigilancias(token) {
    try {
      const url = `${BASE_API}/api/vigilancias/`;
      const params = {
        method: "GET",
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
  // export async function getVigilanciasInactivas(token) {
  //   try {
  //     const url = `${BASE_API}/api/vigilancias/?inactivo=${true}`;
  //     const params = {
  //       method: "GET",
  //       headers: {
  //         Authorization: `Token ${token}`,
  //       },
  //     };
  //     const response = await fetch(url, params);
  //     const result = await response.json();
  //     return result;
  //   } catch (error) {
  //     throw error;
  //   }
  // }
  export async function addTurnosApi(data, token) {
    try {
      const url = `${BASE_API}/api/vigilancia/turnos/`;
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

  export async function getTurno(token,id) {
    try {
      const url = `${BASE_API}/api/vigilancia/turnos/${id}/`;
      const params = {
        method: "GET",
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
  export async function getPersonal(token) {
    try {
      const url = `${BASE_API}/api/personal/`;
      const params = {
        method: "GET",
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
  export async function asignarPersonal(data, token,id) {
    try {
      const url = `${BASE_API}/api/vigilancia/${id}/turnos/`;
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
  export async function deleteVigilanciaApi(id, token) {
    try {
      const url = `${BASE_API}/api/vigilancias/${id}/`;
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
  export async function getTurnosApi(id,token) {
    try {
      const url = `${BASE_API}/api/vigilancia/${id}/turnos/`;
      const params = {
        method: "GET",
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
  export async function deleteHistorialApi(id,id_turno, token) {
    try {
      const url = `${BASE_API}/api/vigilancia/${id}/turnos/${id_turno}/`;
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
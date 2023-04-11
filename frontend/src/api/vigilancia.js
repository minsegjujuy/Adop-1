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
  export async function getJurisdicciones(token) {
    try {
      const url = `${BASE_API}/api/dependencias/`;
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
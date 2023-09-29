import { BASE_API } from "../utils/contants";

//* Base Services
export async function getElementsService(token, model, id = null, subModel = null, subId = null, query = null) {
  try {
    var parametros = query
        ? `?${(() => {
            let paramString = "";
            query.forEach((param) => {
              const key = Object.keys(param)[0]; // Obtiene la clave (primer elemento)
              const value = param[key]; // Obtiene el valor asociado a la clave
              paramString += `${key}=${value}`;
          });
            return paramString;
          })()}`
        : '';
    const url = `${BASE_API}/api/${model.trim()}/${id ? id + "/" : ''}${subModel ? subModel.trim() + '/': ''}${subId ? subId + "/" : ''}${parametros.trim()}`;
    const headers = {
      method: "GET",
      headers: {
        Authorization: `Token ${token}`,
      },
    };
    const response = await fetch(url, headers);
    const result = await response.json();
    console.log(await result);
    return result;
  } catch (error) {
    // throw error;
    return error;
  }
}
export async function getElementService(token, model, id = null, subModel = null, subId = null) {
  try {
    const url = `${BASE_API}/api/${model.trim()}/${id ? id + "/" : ''}${subModel ? subModel.trim() + '/': ''}${subId ? subId + "/" : ''}`;
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
    // throw error;
    return error;
  }
}
export async function addElementService(token, data, model, id = null, subModel = null) {
  try {
    const url = `${BASE_API}/api/${model.trim()}/${id ? id + "/" : ''}${subModel ? subModel.trim() + '/': ''}`;
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
    // throw error;
    return error;
  }
}
export async function updateElementService(token, data, model, id, subModel = null, subId = null) {
  try {
    const url = `${BASE_API}/api/${model.trim()}/${id}/${subModel ? subModel.trim() + '/': ''}${subId ? subId + "/" : ''}`;
    console.log(url);
    const params = {
      method: "PUT",
      headers: {
        Authorization: `Token ${token}`,
      },
      body: JSON.stringify(data),
    };

    const response = await fetch(url, params);
    const result = await response.json();
    return result;
  } catch (error) {
    // throw error;
    return error;
  }
}
export async function deleteElementService(token, model, id, subModel = null, subId = null) {
  try {
    const url = `${BASE_API}/api/${model}/${id}/${subModel ? subModel.trim() + '/': ''}${subId ? subId + "/" : ''}`;
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
    // throw error;
    return error;
  }
}

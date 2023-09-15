import { BASE_API } from "../utils/contants";

//* Base Services
export async function getElementsService(token, model, id = null, subModel = null, subId = null, query = null) {
  try {
    var parametros =
      "" + query
        ? `?${query.forEach((param) => {
            const [key, value] = param;
            parametros += `${key}=${value}`;
          })}`
        : "";

    // var parametros = "";
    // query.forEach((param) => {
    //   const [key, value] = param;
    //   parametros += `${key}=${value}`;
    // });
    // parametros = (query) ? `?${parametros}` :"";

    const url = `${BASE_API}/api/${model}/${id ? id + "/" : ""}
    ${subModel ? (subModel + "/" + subId ? subId + "/" : "") : ""}
    ${parametros}`;
    const headers = {
      method: "GET",
      headers: {
        Authorization: `Token ${token}`,
      },
    };
    const response = await fetch(url, headers);
    const result = await response.json();
    return result;
  } catch (error) {
    throw error;
  }
}
export async function getElementService(token, model, id = null, subModel = null, subId = null) {
  try {
    const url = `${BASE_API}/api/${model}/${id ? id + "/" : ""}
    ${subModel ? (subModel + "/" + subId ? subId + "/" : "") : ""}`;
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
export async function addElementService(token, data, model, id = null, subModel = null) {
  try {
    const url = `${BASE_API}/api/${model}/${id ? id + "/" : ""}
    ${subModel ? subModel + "/" : ""}`;
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
export async function updateElementService(token, data, model, id, subModel = null, subId = null) {
  try {
    const url = `${BASE_API}/api/${model}/${id}/
    ${subModel ? (subModel + "/" + subId ? subId + "/" : "") : ""}`;
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
    throw error;
  }
}
export async function deleteElementService(token, model, id, subModel = null, subId = null) {
  try {
    const url = `${BASE_API}/api/${model}/${id}/
    ${subModel ? (subModel + "/" + subId ? subId + "/" : "") : ""}`;
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

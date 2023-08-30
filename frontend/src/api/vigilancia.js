import {BASE_API} from "../utils/contants"

//* Unidades Regionales
export async function getRegionales(token) {
  try {
    const url = `${BASE_API}/api/unidades_regionales/`;
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

//* Jurisdicciones
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

//* Motivos
export async function getMotivos(token) {
  try {
    const url = `${BASE_API}/api/motivos/`;
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

//* Recursos
export async function getTipoRecursos(token) {
  try {
    const url = `${BASE_API}/api/recursos/`;
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

//* Servicios
export async function getTipoServicios(token) {
  try {
    const url = `${BASE_API}/api/tipo_servicios/`;
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

//* Vigilancias
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

//* Turnos
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
export async function addTurnosApi(data,fk_vigilancia, token) {
  try {
    const url = `${BASE_API}/api/vigilancias/${fk_vigilancia}/turnos/`;
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
export async function getTurnosApi(id,token) {
  try {
    const url = `${BASE_API}/api/vigilancias/${id}/turnos/`;
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
export async function deleteHistorialApi(id, id_turno, token) {
  try {
    const url = `${BASE_API}/api/vigilancias/${id}/turnos/${id_turno}/`;
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

//* Documentos
export async function addDocumentoVigilancia(data, token) {
  try {
    const url = `${BASE_API}/api/vigilancias/documentos/`;
    const params = {
      method: "POST",
      headers: {
        Authorization: `Token ${token}`,
        "Content-Type": "multipart/form-data",
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
export async function getDocumentosVigilancia(id_vigilancia, token) {
  try {
    const url = `${BASE_API}/api/vigilancias/${id_vigilancia}/documentos/`;
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
export async function getDocumentoVigilancia(id_vigilancia, id_documento, token) {
  try {
    const url = `${BASE_API}/api/vigilancias/${id_vigilancia}/documentos/${id_documento}`;
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
export async function updateDocumentoVigilancia(data, id_documento, id_vigilancia, token) {
  try {
    const url = `${BASE_API}/api/vigilancias/${id_vigilancia}/documentos/${id_documento}`;
    const params = {
      method: "PUT",
      headers: {
        Authorization: `Token ${token}`,
      },
      body: JSON.stringify(data)
    };

    const response = await fetch(url, params);
    const result = await response.json();
    return result;
  } catch (error) {
    throw error;
  }
}
export async function deleteDocumentoVigilancia(id_vigilancia, id_documento, token) {
  try {
    const url = `${BASE_API}/api/vigilancias/${id_vigilancia}/documentos/${id_documento}`;
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

//* Personal Turno
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
    const url = `${BASE_API}/api/vigilancias/${id}/turnos/`;
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
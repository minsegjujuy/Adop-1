import {
  getElementService,
  getElementsService,
  addElementService,
  updateElementService,
  deleteElementService,
} from "./baseServides";

import{
  loginService,
  logoutService,
  getTokenService,
} from './authServices';

//* Authentication
export async function loginApi(formValue) {
  return loginService(formValue)
}
export async function logoutApi(token) {
  return logoutService(token);
}
export async function getTokenApi(usuario) {
  return getTokenService(usuario)
}

//* User
export async function getUsersApi(token) {
  return await getElementsService(token, "usuarios");
}
export async function getUserApi(token, id_usuario) {
  return await getElementService(token, "usuarios", id_usuario);
}
export async function addUserApi(data, token) {
  return addElementService(token, data, "usuarios");
}

export async function updateUserApi(token, data, id) {
  return await updateElementService(token, data, "usuarios", id);
}
export async function deleteUserApi(id, token) {
  return await deleteElementService(token, "usuarios", id);
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

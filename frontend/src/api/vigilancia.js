import {
  getElementService,
  getElementsService,
  addElementService,
  updateElementService,
  deleteElementService,
} from "./baseServides";

//* Unidades Regionales
export async function getRegionales(token) {
  return await getElementsService(token, "unidades_regionales");
}

//* Jurisdicciones
export async function getJurisdicciones(token, id) {
  return await getElementsService(token, "dependencias", null, null, null, [{ uurr: id }]);
}

//* Motivos
export async function getMotivos(token) {
  return await getElementsService(token, "motivos");
}

//* Recursos
export async function getTipoRecursos(token) {
  return await getElementsService(token, "recursos");
}

//* Servicios
export async function getTipoServicios(token) {
  return await getElementsService(token, "tipo_servicio");
}

//* Vigilancias
export async function addVigilanciaApi(data, token) {
  return addElementService(token, data, "vigilancias");
}
export async function getVigilancias(token) {
  return await getElementsService(token, "vigilancias");
}
export async function getVigilanciasInactivas(token) {
  return await getElementsService(token, "vigilancias", null, null, null, [{ inactivo: true }]);
}
export async function deleteVigilanciaApi(id, token) {
  return await deleteElementService(token, "vigilancias", id);
}

//* Turnos
export async function getTurno(token, id) {
  return await getElementService(token, "vigilancias", id, "turnos");
}
export async function addTurnosApi(data, id, token) {
  return await addElementService(token, data, "vigilancias", id, "turnos");
}
export async function getTurnosApi(id, token) {
  return await getElementsService(token, "vigilancias", id, "turnos");
}
export async function deleteHistorialApi(id, id_turno, token) {
  return await deleteElementService(token, "vigilancias", id, "turnos", id_turno);
}

//* Documentos
export async function addDocumentoVigilancia(data, token) {
  return await addElementService(token, data, "vigilancias", null, "documentos");
}
export async function getDocumentosVigilancia(id_vigilancia, token) {
  return await getElementsService(token, "vigilancias", id_vigilancia, "documentos");
}
export async function getDocumentoVigilancia(id_vigilancia, id_documento, token) {
  return await getElementService(token, "vigilancias", id_vigilancia, "documentos", id_documento );
}
export async function updateDocumentoVigilancia(data, id_documento, id_vigilancia, token) {
  return await updateElementService(token, data, "vigilancias", id_vigilancia, "documentos", id_documento);
}
export async function deleteDocumentoVigilancia(id_vigilancia, id_documento, token) {
  return await deleteElementService(token, "vigilancias", id_vigilancia, "documentos", id_documento);
}

//* Personal Turno
export async function getPersonal(token) {
  return await getElementsService(token, "personal");
}
export async function asignarPersonal(data, token, id) {
  return await addElementService(token, data, "vigilancias", id, "turnos");
}
